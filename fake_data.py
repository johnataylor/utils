import pandas as pd
from faker import Faker
import random
import xlsxwriter

fake = Faker()

metadata = [
    ["Cell Phone Company:", fake.company()],
    ["Export Date:", fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")],
    ["Tower Region:", fake.city()],
    ["Contact:", fake.name()],
    ["Notes:", "Confidential - Internal Use Only"],
    [],
]

num_rows = 120
data = []
for _ in range(num_rows):
    row = {
        "IMSI": f"310{random.randint(1000000000, 9999999999)}",
        "IMEI": f"{random.randint(100000000000000, 999999999999999)}",
        "Cell_ID": f"{random.randint(10000, 99999)}",
        "Sector_Code": f"SCT-{random.randint(1, 12)}",
        "RSSI_dBm": random.randint(-120, -60),
        "LAC": random.randint(1000, 9999),
        "MCC": random.randint(200, 999),
        "MNC": random.randint(1, 99),
        "Session_ID": f"SID{random.randint(100000,999999)}",
        "Timestamp": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
        "Device_Model": f"Model-{random.choice(['A','B','C','D'])}{random.randint(100,999)}",
        "Firmware_Version": f"{random.randint(1,10)}.{random.randint(0,9)}.{random.randint(0,99)}",
        "Hex_Auth_Token": f"0x{random.randint(0, 2**32):08X}",
        "Uplink_Mbps": round(random.uniform(1, 100), 2),
        "Downlink_Mbps": round(random.uniform(1, 200), 2),
    }
    data.append(row)

df = pd.DataFrame(data)

output_file = "cell_tower_records.xlsx"
logo_file = "logo.png"

with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
    workbook = writer.book
    worksheet = workbook.add_worksheet("Sheet1")
    writer.sheets["Sheet1"] = worksheet

    big_font = workbook.add_format({'font_size': 16, 'bold': True, 'font_color': 'blue'})
    normal_font = workbook.add_format({'font_size': 12})

    for idx, meta_row in enumerate(metadata):
        if meta_row:
            worksheet.write_row(idx, 0, meta_row, big_font)
        else:
            worksheet.write(idx, 0, "", normal_font)

    # try:
    #     worksheet.insert_image(0, 3, logo_file, {'x_scale': 0.5, 'y_scale': 0.5})
    # except Exception as e:
    #     worksheet.write(0, 3, "Logo missing!", big_font)

    df.to_excel(writer, sheet_name="Sheet1", index=False, startrow=len(metadata))

print(f"{output_file} generated. Open it in Excel to see the big fonts and logo.")