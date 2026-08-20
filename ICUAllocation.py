patients = {}
icu_beds = 2
waiting_list = []


def calculate_priority(oxygen, heart_rate, blood_pressure, temperature):
    score = 0

    if oxygen < 90:
        score += 40
    elif oxygen < 94:
        score += 20

    if heart_rate > 120 or heart_rate < 50:
        score += 25

    if blood_pressure < 90:
        score += 20

    if temperature > 39 or temperature < 35:
        score += 15

    if score >= 70:
        return score, "CRITICAL"
    elif score >= 50:
        return score, "HIGH"
    elif score >= 25:
        return score, "MEDIUM"
    else:
        return score, "LOW"


def add_patient(patient_id, age, oxygen, heart_rate,
                blood_pressure, temperature, conditions,
                emergency=False):

    if patient_id in patients:
        return "Duplicate patient"

    if oxygen < 0 or oxygen > 100:
        return "Invalid oxygen level"

    if heart_rate <= 0:
        return "Invalid heart rate"

    score, priority = calculate_priority(
        oxygen, heart_rate, blood_pressure, temperature
    )

    patient = {
        "id": patient_id,
        "age": age,
        "score": score,
        "priority": priority,
        "emergency": emergency
    }

    patients[patient_id] = patient

    if icu_beds > 0 or emergency:
        return allocate_bed(patient_id)

    waiting_list.append(patient_id)
    return "Waiting List"


def allocate_bed(patient_id):
    global icu_beds

    if icu_beds > 0:
        icu_beds -= 1
        return "ICU Bed Allocated"

    if patients[patient_id]["emergency"]:
        return "Emergency Priority"

    waiting_list.append(patient_id)
    return "Waiting List"
