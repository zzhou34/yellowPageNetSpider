import xlwt
import fir_software
import gl
class Outputer():
    def __init__(self):
        self.datas=[]
        self.addresses=[]

    def collect_data(self,new_data,new_address):
        self.datas.append(new_data)
        self.addresses.append(new_address)
        print (new_data)
        print (new_address)
    def output_html(self):
        # font=open('output.html','w',encoding='utf-8')
        # font.write("<html>")
        # font.write("<meta charset='utf-8'>")
        # font.write("<table>")
        #
        # for data in self.datas:
        #     font.write("<tr>")
        #     font.write("<td>%s</td>"%data['url'])
        #     font.write("<td>%s</td>"%data['title'])
        #     font.write("<td>%s</td>"%data['summary'])
        #     font.write("</tr>")
        #
        # font.write("</table>")
        # font.write("</html>")
        book=xlwt.Workbook(encoding='utf-8',style_compression=0)
        sheet=book.add_sheet('coordinates',cell_overwrite_ok=True)
        row_la=0
        row_lo=0
        for data in self.datas:
            #del data[0]
            for coordinate in data:
                sheet.write(row_la,0,coordinate[0])
                sheet.write(row_la,1,coordinate[1])
                row_la=row_la+1
                row_lo=row_lo+1


        book.save(gl.edit2)

        book1=xlwt.Workbook(encoding='utf-8',style_compression=0)
        sheet1=book1.add_sheet('addresses',cell_overwrite_ok=True)
        row_ad1=0
        row_ad2=0
        row_city=0
        row_state=0
        row_zip=0
        row_full=0
        for address in self.addresses:
            for add in address:
                sheet1.write(row_ad1,0,add[0])
                sheet1.write(row_ad2,1,add[1])
                sheet1.write(row_city,2,add[2])
                sheet1.write(row_state,3,add[3])
                sheet1.write(row_zip,4,add[4])
                sheet1.write(row_full,5,add[5])
                row_ad1=row_ad1+1
                row_ad2=row_ad2+1
                row_city=row_city+1
                row_state=row_state+1
                row_zip=row_zip+1
                row_full=row_full+1
        book1.save(gl.edit3)