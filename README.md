# Matching Game Card API
เป็น Service API สำหรับเกมจับคู่ ซึ่งสร้างด้วย FastAPI

## ก่อนติดตั้ง

ให้ไปตั้งค่า SecretKey ของ API ด้วยการสร้าง Hex string ด้วยคำสั่ง

```bash
openssl rand -hex 32
```
 จากนั้นในไปใส่ใน File .env
```bash
SECRET_KEY=Hex String ที่สร้างมา
```

## ขั้นตอนการติดตั้ง

1. ลง docker และ docker-compose ในเครื่อง
2. Clone repository นี้ไปยังเครื่อง Production
3. ใช้คำสั่ง docker-compose build
4. ใช้คำสั่ง docker-compose up
5. สามารถใช้ API ได้จากพอร์ท 8000 ได้เลย

## ข้อมูลการใช้งาน API

| API Name | Method | คำอธิบาย | ค่าที่ส่งใน body/request | จำเป้นต้องใส่ Token ใน Header |
| ------ | ------ | ------ | ------ | ------ |
| /get_token | POST | เป็น API ที่ส่งค่า username มาเพื่อที่รับ Token ใช้ในการยืนยันตัวตนในระบบ | {"username":ชื่อusername} | ไม่ |
| /start_new_game | POST | เป็น API สำหรับใช้กับปุ่มเริ่มเล่นเกมโดยการส่ง | - | จำเป็น |

## ข้อมูลการใช้งาน Web Socket

| Socket Name | คำอธิบาย |
| ------ | ------ |
| /playgame | เป็น WebSocket ที่ติดต่อส่งข้อมูลในระหว่างเกม |

โดยการใช้งานของ Websocket นี้จะเป้นขั้นตอนดังนี้

1. ให้ส่งค่า Token ไปเพื่อทำการเริ่มการก่อนระบบจะเช็ค Username จาก Token แล้วส่งค่า Global Score และ Best score ของผู้เล่นนั้นมา (ซึ่งในจุดนี้แปลว่า คุณได้ทำการเชื่อมต่อ Websocket สำเร็จแล้ว)
