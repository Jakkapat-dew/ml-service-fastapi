from typing import Annotated
from fastapi import APIRouter, File, UploadFile, Response
from controlers.data_getting import DataAccess

# class method from controllers
clsDataAccess = DataAccess()

# Router or Sub-API
dataGetting = APIRouter(prefix="/dataGetting",
                        tags=["dataGetting"],
                        )

@dataGetting.post("/read_csv/")
async def read_csv(file: UploadFile):
    df = clsDataAccess.data_from_csv(csv_file=file)
    return Response(df.to_json(orient="records"), media_type="application/json")