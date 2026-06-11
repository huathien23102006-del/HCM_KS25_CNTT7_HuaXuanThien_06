

def menu():
    print("==== BOOKING ====")
    print("="*20)
    print("1. Hiển thị danh sách lịch đặt")
    print("2. Đăng ký lịch đặt phòng mới")
    print("3. Cập nhật thông tin lịch hẹn")
    print("4. Hủy/Xóa lịch đặt phòng")
    print("5. Tìm kiếm lịch đặt phòng")
    print("6. Thống kê mật độ sử dụng")
    print("7. Phân loại khung giờ tự động")
    print("8. Thoát chương trình")
    print("="*20)

def show_booking(books):
        print("====DANH SÁCH ĐẶT PHÒNG====")
        print(f"{"Mã BK":<9} | {"Tên phòng":<20} | {"Người đặt":<20} | {"Giờ bắt đầu":<20} | {"Giờ kết thúc":<20} | {"Thời lượng":<15} | {"Phân loại":<20}")
        print("="*120)
        for item in books:
            print(f"{item["id"]:<8} | {item["name"]:<20} | {item["user"]:<20} | {item["start"]:<20} | {item["end"]:<20} | {item["time"]:<15} | {item["class"]:<20}")
        print("="*120)

def booking_new(books):
    while True:
        input_id = input("Nhập vào mã BK: ")
        if not input_id:
            print("Mã BK không được để trống!")
            continue
        for item in books:
            if(input_id.lower() == item.get("id").lower()):
                print("Mã không được trùng!")
                break

        input_name = input("Nhập tên phòng: ")
        if not input_name:
            print("Tên phòng không được để trống")
            continue
        input_user = input("Nhập tên người đặt/phòng ban: ")
        if not input_user:
            print("Tên người đặt/phòng ban không được để trống!")
            continue
        input_start = int(input("Nhập giờ bắt đầu: "))
        if(input_start < 0 or input_start > 24):
            print("Thời gian bắt đầu phải là số nguyên dương và trong khoảng 0-24!")
            continue
        input_end = int(input("Nhập giờ kết thúc: "))
        if(input_end < 0 or input_end > 24):
            print("Thời gian bắt đầu phải là số nguyên dương và trong khoảng 0-24!")
            continue

        elif(input_end < input_start):
            print("Giờ kết thúc phải lớn hơn giờ bắt đầu")
            continue
        else:
            time = (input_end - input_start)
        if time < 2:
            class_bk = "Ngắn"
            break
        elif time >= 2 and time < 4:
            class_bk = "Tiêu chuẩn"
            break
        elif time >= 4 and time < 6:
            class_bk = "Dài"
            break
        else:
            class_bk = "Quá tải (Cần xem xét lại)"
            break
    new_list = {
        "id": input_id,
        "name": input_name,
        "user": input_user,
        "start": input_start,
        "end": input_end,
        "time": time,
        "class": class_bk
    }
    books.append(new_list)



def main():
    booking = [{"id": "BK001",
            "name": "Phòng Thảo Luận A",
            "user": "Phòng Marketing",
            "start": 9,
            "end": 12,
            "time": 3,
            "class": "Tiêu chuẩn"
        }]
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn (1-8): ")
        match choice:
            case "1":
                show_booking(booking)
            case "2":
                booking_new(booking)
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass
            case "8":
                print("Kết thúc chương trình!")
                break
            case _:
                print("Lựa chọn không hợp lệ")

main()
