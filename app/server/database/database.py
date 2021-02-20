import motor.motor_asyncio
from bson import ObjectId
from decouple import config

MONGO_URL = config('DB_URL')
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = client.Sangkuriang

# Scanner database handler
scan_results = database.get_collection('scan_results')

def scan_results(scan) -> dict:
    return {
        "id": str(scan['_id']),
        "target": scan['url'],
        "results": scan['reults'],
    }

def scan_id(scan) -> dict:
    return {
        "id": str(scan['_id']),
    }

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