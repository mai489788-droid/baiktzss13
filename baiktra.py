staffs = []
next_id = 101

while True:
    print("QUẢN LÝ NHÂN SỰ - STAFF MANAGER")
    print("1. Thêm nhân viên mới")
    print("2. Danh sách nhân viên")
    print("3. Tìm kiếm nhân viên (Theo mã)")
    print("4. Xóa nhân viên khỏi hệ thống")
    print("5. Thoát chương trình")

    choose = int(input("Mời bạn nhập lựa chọn: "))

    match choose:

        case 1:
            new_mannager = input("Mời bạn nhập tên: ")

            while new_mannager == "":
                new_mannager = input("Tên không được để trống, nhập lại: ")

            salary = float(input("Nhập lương: "))

            while salary <= 0:
                salary = float(input("Mức lương phải là số dương (>0), nhập lại: "))

            staffs.append({
                "id": next_id,
                "name": new_mannager,
                "salary": salary
            })

            print(f"Thêm nhân viên thành công! ID: {next_id}")

            next_id += 1

        case 2:
            if len(staffs) == 0:
                print("Chưa có dữ liệu nhân sự!")
            else:
                print("\nDANH SÁCH NHÂN VIÊN")

                for employee in staffs:
                    print(employee)

        case 5:
            print("Thoát chương trình")
            break