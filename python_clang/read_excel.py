import sys
try:
    import xlrd
except ModuleNotFoundError as err:
    print(f"{err.msg}")



def show_sheet_by(sheet, way="row"):
    row_num, col_num = sheet.nrows, sheet.ncols
    if "row" == way:
        for _nr in range(row_num):
            rows = sheet.row_values(_nr)
            print(rows)
    elif "col" == way:
        for _nc in range(col_num):
            cols = sheet.col_values(_nc)
            print(cols)


def show_file_page_data(file_name, num_page):
    workbook = xlrd.open_workbook(file_name)
    sheet_name = workbook.sheet_names()[num_page]

    print(f"now you see is: {sheet_name}")

    sheet = workbook.sheet_by_name(sheet_name)
    # show_sheet_by(sheet, "row")
    show_sheet_by(sheet, "col")
    pass

if __name__ == "__main__":
    num_para = len(sys.argv)
    if 1 == num_para or 0 == num_para:
        print("please input aim file name.")
    else:
        try:
            page_num = sys.argv[2] = int(sys.argv[2])
        except:
            page_num = 0
        if 2 == num_para: 
            file_name, page_num = sys.argv[1], 0
        elif 3 == num_para:
            file_name, page_num = sys.argv[1], page_num
        else:
            file_name, page_num = sys.argv[1], page_num
        show_file_page_data(file_name, page_num)
