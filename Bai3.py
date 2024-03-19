from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import plotly.graph_objects as go
import random
import anvil.server
import time

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.arr = [random.randint(10, 100) for _ in range(10)]
    
  def btn_Bubble_click(self, **event_args):
    self.arr = [int(num.strip()) for num in self.txt_arr.text.split(',') if num.strip().isdigit()]
    n = len(self.arr)
    for i in range(n - 1):
      # Tìm phần tử nhỏ nhất trong phần chưa được sắp xếp
      min_index = i
      for j in range(i + 1, n):
        if self.arr[j] < self.arr[min_index]: 
          min_index = j 
      # Hoán đổi phần tử nhỏ nhất với phần tử đầu tiên chưa được sắp xếp
      self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]

    self.lb_output.text = ""
    for i in range(len(self.arr)):
      self.lb_output.text += str(self.arr[i]) + ' '

  pass

  def is_integer_sequence(self, input_str):
    # Tách chuỗi thành danh sách các phần tử
    elements = input_str.split(',')
    # Lặp qua từng phần tử để kiểm tra xem có phải là số nguyên không
    for element in elements:
        element = element.strip()  # Loại bỏ khoảng trắng xung quanh phần tử
        if not element.isdigit():
            return False
    return True

  def txt_arr_change(self, **event_args):
    if self.is_integer_sequence(self.txt_arr.text):
      self.btn_Bubble.enabled = True
      self.btn_Isertion.enabled = True
      self.btn_Selection.enabled = True
    else:
      self.btn_Bubble.enabled = False
      self.btn_Isertion.enabled = False
      self.btn_Selection.enabled = False
    pass

  def btn_Isertion_click(self, **event_args):
    self.arr = [int(num.strip()) for num in self.txt_arr.text.split(',') if num.strip().isdigit()]
    # Lặp qua từng phần tử trong danh sách
    for i in range(1, len(self.arr)):
      key = self.arr[i]
      # Di chuyển các phần tử của danh sách đã được sắp xếp về phía trước
      # để tìm vị trí thích hợp cho phần tử hiện tại (key)
      j = i - 1
      while j >= 0 and key < self.arr[j]:
        self.arr[j + 1] = self.arr[j]
        j -= 1
      # Chèn phần tử vào vị trí đã tìm được
      self.arr[j + 1] = key

    self.lb_output.text = ""
    for i in range(len(self.arr)):
      self.lb_output.text += str(self.arr[i]) + ' '
    pass

  def btn_Selection_click(self, **event_args):
    self.arr = [int(num.strip()) for num in self.txt_arr.text.split(',') if num.strip().isdigit()]
    n = len(self.arr)
    for i in range(n - 1):
      # Tìm phần tử nhỏ nhất trong phần chưa được sắp xếp
      min_index = i
      for j in range(i + 1, n):
        if self.arr[j] < self.arr[min_index]: 
          min_index = j
          
      # Hoán đổi phần tử nhỏ nhất với phần tử đầu tiên chưa được sắp xếp
      self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]

    self.lb_output.text = ""
    for i in range(len(self.arr)):
      self.lb_output.text += str(self.arr[i]) + ' '
    pass
