from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timezone

app = FastAPI(title="Well Health Care API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

appointments = []


class Appointment(BaseModel):
    name: str
    email: str
    service: str
    date: str


@app.get("/")
def home():
    return {
        "message": "Welcome to the Well Health Care API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "well-health-care-backend",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get("/services")
def get_services():
    return {
        "services": [
            {
                "id": 1,
                "name": "Primary Care",
                "description": "General health consultations and routine checkups."
            },
            {
                "id": 2,
                "name": "Telehealth",
                "description": "Virtual appointments with healthcare providers."
            },
            {
                "id": 3,
                "name": "Lab Requests",
                "description": "Schedule and manage diagnostic lab services."
            }
        ]
    }


@app.post("/appointments")
def create_appointment(appointment: Appointment):
    new_appointment = {
        "id": len(appointments) + 1,
        "name": appointment.name,
        "email": appointment.email,
        "service": appointment.service,
        "date": appointment.date,
        "status": "received"
    }

    appointments.append(new_appointment)

    return {
        "message": "Appointment request received successfully",
        "appointment": new_appointment
    }


@app.get("/appointments")
def get_appointments():
    return {
        "count": len(appointments),
        "appointments": appointments
    }