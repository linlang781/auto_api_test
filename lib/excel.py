#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: excel.py.py
@time: 17-3-31 上午1:34
"""
import xlrd


class XlsOpreate(object):
    """
    封装常用Xls操作
    """

    def __init__(self, xlsname):
        """
        定义类的变量
        """
        self.xlsname = xlsname

        self.xlrd_object = xlrd.open_workbook(self.xlsname)

    def getsheets(self):
        """
        获取Xls的Sheet
        :return sheet list
        """
        return self.xlrd_object.sheet_names()

    def getrows(self, sheetname):
        """
        获取sheet页行数
        """
        worksheet = self.xlrd_object.sheet_by_name(sheetname)
        return worksheet.nrows

    def getcols(self, sheetname):
        """
        获取sheet页列数
        """
        worksheet = self.xlrd_object.sheet_by_name(sheetname)
        return worksheet.ncols

    def readrow(self, sheetname, rown):
        """
        获取一行数据
        """
        worksheet = self.xlrd_object.sheet_by_name(sheetname)
        return worksheet.row_values(rown)

    def readcol(self, sheetname, coln):
        """
        获取一列数据
        """
        worksheet = self.xlrd_object.sheet_by_name(sheetname)
        return worksheet.col_values(coln)

    def readcell(self, sheetname, rown, coln):
        """
        获取指定坐标的数据
        """
        worksheet = self.xlrd_object.sheet_by_name(sheetname)
        return worksheet.cell_value(rown, coln)

    def writecell(self, sheetn, rown, coln, value):
        """
        write a cell to file,other cell is not change
        """
        pass
