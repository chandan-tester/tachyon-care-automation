import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    ORG_NAME = os.getenv("ORG_NAME", "williams")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "app-stage")
    BASE_URL = f"https://{ORG_NAME}.{ENVIRONMENT}.tachyoncare.io"

    USERS = {
        "admin": (os.getenv("ADMIN_EMAIL"), os.getenv("ADMIN_PASSWORD")),
        "care_manager": (os.getenv("CARE_MANAGER_EMAIL"), os.getenv("CARE_MANAGER_PASSWORD")),
        "care_coordinator": (os.getenv("CARE_COORDINATOR_EMAIL"), os.getenv("CARE_COORDINATOR_PASSWORD")),
        "nurse": (os.getenv("NURSE_EMAIL"), os.getenv("NURSE_PASSWORD")),
        "technician": (os.getenv("TECHNICIAN_EMAIL"), os.getenv("TECHNICIAN_PASSWORD")),
    }