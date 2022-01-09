import time
import json

import serial


def wait_response(ser, timeout=5):
    start = time.time()
    empty_num = 0
    while True:
        resp = ser.readline()
        #print(resp)
        if resp == "".encode():
            empty_num += 1
        elif resp == "\r\n".encode():
            pass
        else:
            print("↓", resp[:-2].decode())

        if time.time() - start > timeout:
            break



def send_command(ser, command, end="\r\n"):
    ser.write(f"{command}{end}".encode())
    print("↑", command)


with serial.Serial('COM14', 115200, timeout=1) as ser:
    send_command(ser, "AT")
    wait_response(ser)
    send_command(ser, "AT+CWJAP=\"WiFi18\",\"Bigamy030390\"")
    wait_response(ser, timeout=20)
    send_command(ser, "AT+CIPMUX=1")
    wait_response(ser, timeout=5)
    send_command(ser, "AT+CIPSERVER=1,5000")
    wait_response(ser, timeout=5)
    send_command(ser, "AT+CIPSTO=3600")
    wait_response(ser, timeout=5)
    send_command(ser, "AT+CIPSTA_CUR?")
    wait_response(ser, timeout=5)

    # send_command(ser, f"AT+CIPSTART=0,\"TCP\",\"192.168.1.101\",80")
    # wait_response(ser, timeout=5)
    #
    # data_message = json.dumps({"status": "OK"})
    # data = f"GET /index HTTP/1.1\r\n" \
    #        f"Accept:application/json, text/plain, */*\r\n" \
    #        f"Content-Type:application/json;charset=UTF-8\r\n" \
    #        f"Content-Length: {len(data_message)}\r\n" \
    #        f"\r\n" \
    #        f"{data_message}"
    #
    # send_command(ser, f"AT+CIPSEND=0,{len(data)+4}")
    # wait_response(ser, timeout=5)
    # send_command(ser, data)
    # send_command(ser, "AT+CIPCLOSE=0")
