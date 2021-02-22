from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import app.database
import app.models
from app.models.scan import *
from app.modules.nmap import *
from app.modules.owaspzap import *
from app.modules.chaos import *

router = APIRouter()

@router.get("/", response_description="Scan retrieved")
async def get_scan():
	scan = await retrieve_all_scan()
	return ResponseModel(scan, "Scan data retrieved successfully") \
		if len(scan) > 0 \
		else ResponseModel(
		scan, "Empty list")


# @router.get("/details/{id}", response_description="Scan data retrieved")
# async def get_scan_data_by_id(id):
# 	scan = await retrieve_scan_by_id(id)
# 	return ResponseModel(scan, "Scan data retrieved successfully with id {0}") \
# 		if scan \
# 		else ErrorResponseModel("An error occured.", 404, "Scan with id {0} doesn'exist.")

# @router.post("/", response_description="Scan data added into the database")
# async def add_scan_data(scan_data: ScanModel = Body(...)):
# 	scan = jsonable_encoder(scan_data)
# 	new_scan = await add_scan(scan)
# 	return ResponseModel(new_scan, "Scan added successfully.")


# @router.delete("/{id}", response_description="Scan data deleted from the database")
# async def delete_scan_data(id: str):
# 	deleted_scan = await delete_scan(id)
# 	return ResponseModel("Student with ID: {} removed".format(id), "Student deleted successfully") \
# 		if deleted_scan \
# 		else ErrorResponseModel("An error occured", 404, "Scan with id {0} doesn't exist".format(id))

# Please put you development module in here

# NMAP Scanner author : @arkwrn
@router.post("/nmap/{target}/top-port", response_description="Port scanner")
async def check_open_port(target):
	scan = port_scanner(target)
	return scan \
		if scan \
		else ErrorResponseModel("An error occured.", 404, "Target not response / invalid.")


#Scan for zap proxy author : @wahyuhadi
@router.post("/zap/{target}/spider", response_description="Start spider web scanner and return id")
async def spider_scan(target):
	try:
		isTarget = "https://{}".format(target)
		scan = spider_mode(isTarget)
		return scan \
			if scan \
			else ErrorResponseModel("An error occured.", 404, "Target not response / invalid.")
	except:
		ErrorResponseModel("An error occured.", 404, "Something wrong.")

# NMAP Scanner author : @arkwrn
@router.post("/subdomains/{target}/", response_description="Subdomain enumeration")
async def check_subdomain(target):
	scan = chaos_client(target, 'json')
	return scan \
		if scan \
		else ErrorResponseModel("An error occured.", 404, "Target not response / invalid.")