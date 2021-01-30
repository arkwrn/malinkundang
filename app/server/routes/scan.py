from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.server.database.database import *
from app.server.models.scan import *
from app.server.modules.nmap import *

router = APIRouter()

@router.get("/", response_description="Scan retrieved")
async def get_scan():
	scan = await retrieve_all_scan()
	return ResponseModel(scan, "Scan data retrieved successfully") \
		if len(scan) > 0 \
		else ResponseModel(
		scan, "Empty list")


@router.get("/details/{id}", response_description="Scan data retrieved")
async def get_scan_data_by_id(id):
	scan = await retrieve_scan_by_id(id)
	return ResponseModel(scan, "Scan data retrieved successfully with id {0}") \
		if scan \
		else ErrorResponseModel("An error occured.", 404, "Scan with id {0} doesn'exist.")

@router.post("/", response_description="Scan data added into the database")
async def add_scan_data(scan_data: ScanModel = Body(...)):
	scan = jsonable_encoder(scan_data)
	new_scan = await add_scan(scan)
	return ResponseModel(new_scan, "Scan added successfully.")


@router.delete("/{id}", response_description="Scan data deleted from the database")
async def delete_scan_data(id: str):
	deleted_scan = await delete_scan(id)
	return ResponseModel("Student with ID: {} removed".format(id), "Student deleted successfully") \
		if deleted_scan \
		else ErrorResponseModel("An error occured", 404, "Scan with id {0} doesn't exist".format(id))


@router.put("/{id}")
async def update_scan(id: str, req: UpdateScanModel = Body(...)):
	updated_scan = await update_scan_data(id, req.dict())
	return ResponseModel("Student with ID: {} name update is successful".format(id),
						 "Student name updated successfully") \
		if updated_scan \
		else ErrorResponseModel("An error occurred", 404, "There was an error updating the student.".format(id))


# Please put you development module test in here
@router.get("/nmap/{target}", response_description="Port scanner")
async def check_open_port(target):
	scan = port_scanner(target)
	return scan \
		if scan \
		else ErrorResponseModel("An error occured.", 404, "Scan with id {0} doesn'exist.")