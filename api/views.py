from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from appointment.models import Department, timeTable, Appointment
from Authentication.models import Doctor, Patient, UserProfile
from Visit.models import PatientVisitInfo, Prescription
from Disease.models import Disease
from Medicine.models import Medicine  
from api.serializers import *


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def department_list(request):
    """
    List all Departments, or create a new Department.
    """
    if request.method == 'GET':
        Departments = Department.objects.all()
        serializer = DepartmentSerializer(Departments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def department_detail(request, pk):
    """
    Get, udpate, or delete a specific Department
    """
    try:
        Departments = Department.objects.get(pk=pk)
    except Departments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DepartmentSerializer(Departments)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DepartmentSerializer(Departments, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Departments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def timeTable_list(request):
    """
    List all timeTables, or create a new timeTable.
    """
    if request.method == 'GET':
        timeTables = timeTable.objects.all()
        serializer = timeTableSerializer(timeTables, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = timeTableSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def timeTable_detail(request, pk):
    """
    Get, udpate, or delete a specific timeTable
    """
    try:
        timeTables = timeTable.objects.get(pk=pk)
    except timeTables.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = timeTableSerializer(timeTables)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = timeTableSerializer(timeTables, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        timeTables.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def appointment_list(request):
    """
    List all Appointments, or create a new Appointment.
    """
    if request.method == 'GET':
        Appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(Appointments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AppointmentSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def appointment_detail(request, pk):
    """
    Get, udpate, or delete a specific Appointment
    """
    try:
        Appointments = Appointment.objects.get(pk=pk)
    except Appointments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentSerializer(Appointments)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AppointmentSerializer(Appointments, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Appointments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def doctor_list(request):
    """
    List all Doctors, or create a new Doctor.
    """
    if request.method == 'GET':
        Doctors = Doctor.objects.all()
        serializer = DoctorSerializer(Doctors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DoctorSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def doctor_detail(request, pk):
    """
    Get, udpate, or delete a specific Doctor
    """
    try:
        Doctors = Doctor.objects.get(pk=pk)
    except Doctors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorSerializer(Doctors)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DoctorSerializer(Doctors, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Doctors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def patient_list(request):
    """
    List all Patients, or create a new Patient.
    """
    if request.method == 'GET':
        Patients = Patient.objects.all()
        serializer = PatientSerializer(Patients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def patient_detail(request, pk):
    """
    Get, udpate, or delete a specific Patient
    """
    try:
        Patients = Patient.objects.get(pk=pk)
    except Patients.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(Patients)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PatientSerializer(Patients, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Patients.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def userProfile_list(request):
    """
    List all UserProfiles, or create a new UserProfile.
    """
    if request.method == 'GET':
        UserProfiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(UserProfiles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserProfileSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def userProfile_detail(request, pk):
    """
    Get, udpate, or delete a specific UserProfile
    """
    try:
        UserProfiles = UserProfile.objects.get(pk=pk)
    except UserProfiles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserProfileSerializer(UserProfiles)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserProfileSerializer(UserProfiles, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        UserProfiles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def patientVisitInfo_list(request):
    """
    List all PatientVisitInfos, or create a new PatientVisitInfo.
    """
    if request.method == 'GET':
        PatientVisitInfos = PatientVisitInfo.objects.all()
        serializer = PatientVisitInfoSerializer(PatientVisitInfos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PatientVisitInfoSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def patientVisitInfo_detail(request, pk):
    """
    Get, udpate, or delete a specific PatientVisitInfo
    """
    try:
        PatientVisitInfos = PatientVisitInfo.objects.get(pk=pk)
    except PatientVisitInfos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientVisitInfoSerializer(PatientVisitInfos)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PatientVisitInfoSerializer(PatientVisitInfos, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        PatientVisitInfos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def prescription_list(request):
    """
    List all Prescriptions, or create a new Prescription.
    """
    if request.method == 'GET':
        Prescriptions = Prescription.objects.all()
        serializer = PrescriptionSerializer(Prescriptions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PrescriptionSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def prescription_detail(request, pk):
    """
    Get, udpate, or delete a specific Prescription
    """
    try:
        Prescriptions = Prescription.objects.get(pk=pk)
    except Prescriptions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PrescriptionSerializer(Prescriptions)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PrescriptionSerializer(Prescriptions, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Prescriptions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def disease_list(request):
    """
    List all Diseases, or create a new Disease.
    """
    if request.method == 'GET':
        Diseases = Disease.objects.all()
        serializer = DiseaseSerializer(Diseases, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DiseaseSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def disease_detail(request, pk):
    """
    Get, udpate, or delete a specific Disease
    """
    try:
        Diseases = Disease.objects.get(pk=pk)
    except Diseases.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DiseaseSerializer(Diseases)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DiseaseSerializer(Diseases, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Diseases.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def medicine_list(request):
    """
    List all Medicines, or create a new Medicine.
    """
    if request.method == 'GET':
        Medicines = Medicine.objects.all()
        serializer = MedicineSerializer(Medicines, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MedicineSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def medicine_detail(request, pk):
    """
    Get, udpate, or delete a specific Medicine
    """
    try:
        Medicines = Medicine.objects.get(pk=pk)
    except Medicines.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MedicineSerializer(Medicines)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MedicineSerializer(Medicines, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Medicines.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
