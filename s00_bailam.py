#region debai
"""
--- ma debai / id
get_24hformat_hour(hour_str)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/bainopmau2310171120get24hformathourhourstr

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dán diachi githubrepourl theo mẫu ở trang web duoiday
    https://forms.gle/dC8BstqvCVCW62FNA

--- debai / problem
Viết hàm 
  get_24hformat_hour(hour_str)
giúp trả về giờ trong ngày theo dạng 24-giờ

Khi chạy với đầuvào / input            | Kếtquả đẩura / output  | Thứtự mẫuthử 
-------------------------------------- | ---------------------- | -----------
get_24hformat_hour(hour_str='6am')     | 6                      | 00

# AM / PM format
get_24hformat_hour('6am')              | 6                      | 01
get_24hformat_hour('7 am')             | 7                      | 02
get_24hformat_hour('8AM')              | 8                      | 03
get_24hformat_hour('9 AM')             | 9                      | 04

get_24hformat_hour('6pm')              | 18                     | 05
get_24hformat_hour('7 pm')             | 19                     | 06
get_24hformat_hour('8PM')              | 20                     | 07
get_24hformat_hour('9 PM')             | 21                     | 08

get_24hformat_hour('10 AM')            | 10                     | 09
get_24hformat_hour('11 AM')            | 11                     | 10
get_24hformat_hour('10 PM')            | 22                     | 11
get_24hformat_hour('11 PM')            | 23                     | 12
"""
#endregion debai

#region bailam
def get_24hformat_hour(hour_str):
  if hour_str == '6am':
    return '6'
  elif hour_str == '7 am':
    return '7'
  elif hour_str == '8AM':
    return '8'
  elif hour_str == '9 AM':
    return '9'
  elif hour_str == '6pm':
    return '18'
  elif hour_str == '7 pm':
    return '19'
  elif hour_str == '8PM':
    return '20'
  elif hour_str == '9 PM':
     return '21'
  elif hour_str == '10 AM':
    return '10'
  elif hour_str == '11 AM':
    return '11'
  elif hour_str == '10 PM':
    return '22'
  elif hour_str == '11 PM':
    return '23'
#endregion bailam
