from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class ScanModel(BaseModel):
	target: str = Field(...)
	results: str = Field(...)

	class Config:
		schema_extra = {
			"example": {
				"target": "http://localhost",
				"results": "Vulnerable XSS",
			}
		}


class UpdateScanModel(BaseModel):
	target: str = Field(...)
	results: str = Field(...)

	class Config:
		schema_extra = {
			"example": {
				"target": "http://localhost",
				"results": "Vulnerable XSS",
			}
		}

def ResponseModel(data, message):
	return {
		"data": [
			data
		],
		"code": 200,
		"message": message,
	}


def ErrorResponseModel(error, code, message):
	return {
		"error": error,
		"code": code,
		"message": message
	}