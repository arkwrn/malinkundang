import motor.motor_asyncio
from bson import ObjectId
from decouple import config

from app.database.database_helper import *

MONGO_DETAILS = config('MONGO_DETAILS')
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.Sangkuriang
scan_results = database.get_collection('scan_results')
admin_collection = database.get_collection('admins')

async def add_admin(admin_data: dict) -> dict:
    admin = await admin_collection.insert_one(admin_data)
    new_admin = await admin_collection.find_one({"_id": admin.inserted_id})
    return admin_helper(new_admin)

# All of the functions below is not tested yet
async def retrieve_all_scan():
    scans = []
    async for scan in scan_results.find():
        scans.append(scan_results(scan))
    return scans

async def add_scan(scan_data: dict) -> dict:
    scan = await scan_results.insert_one(scan_data)
    new_scan = await scan_results.find_one({"_id": scan.inserted_id})
    return scan_results(new_scan)

async def retrieve_scan(id: str) -> dict:
    scan = await scan_results.find_one({"_id": ObjectId(id)})
    if scan:
        return scan_results(scan)

async def retrieve_scan_by_id(id: str) -> dict:
    scan = await scan_results.find_one({"_id": ObjectId(id)})
    if scan:
        return scan_id(scan)

async def delete_scan(id: str):
    scan = await scan_results.find_one({"_id": ObjectId(id)})
    if scan:
        await scan_results.delete_one({"_id": ObjectId(id)})
        return True

async def update_scan_data(id: str, data: dict):
    scan = await scan_results.find_one({"_id": ObjectId(id)})
    if scan:
        scan_results.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True
