
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

def admin_helper(admin) -> dict:
    return {
        "id": str(admin['_id']),
        "fullname": admin['fullname'],
        "email": admin['email'],
    }
