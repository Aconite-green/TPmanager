from time import sleep
import can



# CAN 버스 설정
bus = can.interface.Bus(interface='vector', channel="0, 1", receive_own_messages=True, bitrate=500000, app_name=None)

# 메시지 송신
msg = can.Message(arbitration_id=0x123, data=[0x11, 0x22, 0x33], is_extended_id=False)
# bus.send(msg)
# print("Message sent")
# 
# # 메시지 수신
# message = bus.recv(timeout=10)
# if message:
#     print(f"Received message:")
#     print(f"  ID: {hex(message.arbitration_id)}")
#     print(f"  Data: {message.data}")
#     print(f"  Timestamp: {message.timestamp}")
# else:
#     print("No message received")
# sleep(10)
bus.shutdown()
