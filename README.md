# Matching Game Card API
เป็น Service API สำหรับเกมจับคู่ ซึ่งสร้างด้วย FastAPI

## ก่อนติดตั้ง

ให้ไปตั้งค่า SecretKey ของ API ด้วยการสร้าง Hex string ด้วยคำสั่ง

```bash
openssl rand -hex 32
```
 จากนั้นในไปใส่ใน File .env
```bash
SECRET_KEY=<Hex String ที่สร้างมา>
```

## ขั้นตอนการติดตั้ง

1. ลง docker และ docker-compose ในเครื่อง
2. Clone repository นี้ไปยังเครื่อง Production
3. ใช้คำสั่ง docker-compose build
4. ใช้คำสั่ง docker-compose up
5. สามารถใช้ API ได้จากพอร์ท 8000 ได้เลย

## ข้อมูล API

| API Name | Method | คำอธิบาย | ค่าที่ส่งใน body/request |
| ------ | ------ | ------ | ------ |
| /get_token | POST | เป็น API ที่ส่งค่า username มาเพื่อที่รับ Token ใช้ในการยืนยันตัวตนในระบบ | {"username":<username>} |
| /start_new_game | POST | เป็น API สำหรับใช้กับปุ่มเริ่มเล่นเกมโดยการส่ง Token ที่ได้จาก /get_token ใน Authentication Header |  |

## ข้อมูล Web Socket

| API Name | Method | คำอธิบาย | ค่าที่ส่งใน body/request |
| ------ | ------ | ------ | ------ |
