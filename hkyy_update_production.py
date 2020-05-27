import os
import sqlite3 as db
import csv
import sys
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XMLParser
import time


product_file = r"G:\电子码导入导出目录\03导出目录\products.xml"
db_file = r"G:\电子码导入导出目录\03导出目录\products.db"
sql_file = r"G:\电子码导入导出目录\03导出目录\db.create.sql"
db_not_exists = not os.path.exists(db_file)

sql = rf"""
    insert into hkyy_cxd_proudcts (
        id,productcode,productname,productcomment,typeno,authorizedno,type,specific,
        packagespecific,packageunit,physicdetailtype,codeverion,codelevel,
        packageratio,resourcecode,opuser,bak
    )
    values (
        null, :productCode, :productName, :comment, :typeNo, :authorizedNo,
        :type, :spec, :packageSpec, :packUnit, :physicDetailType, 
        :codeVersion, :codeLevel, :pkgRatio, :resourceCode, '', ''
        )

"""


def InsertIntoDB(db_file, data):
    with db.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.executemany(sql, data)
        # print(sql)


def CreateNewDB():
    with open(sql_file, "rt", encoding="utf-8") as fin, db.connect(db_file) as conn:

        schema = fin.read()

        print("Create DB File...")
        conn.executescript(schema)
        print("OK...")


def GetAllProduct(tree):
    for node in tree.findall(".//product"):
        yield node


def GetAllSubType(tree):
    for node in tree.findall(".//subType"):
        yield node


def GetAllResCode(tree):
    for node in tree.findall(".//resProdCodes//resCode"):
        yield node


def ReadProductXML(file, output_file=sys.stdout):

    with open(product_file, "rt", encoding="utf-8") as fin:
        tree = ET.parse(fin)
        products = []

        for product in GetAllProduct(tree):
            # for k, v in product.attrib.items():
            #    print(k, v)

            for sub_product in GetAllSubType(product):
                # for k, v in sub_product.attrib.items():
                #    print(k, v)
                for rescode in GetAllResCode(sub_product):

                    # print(rescode.text)
                    d = dict()
                    d.update(
                        {
                            "resourceCode".format(
                                rescode.attrib.get("codeLevel")
                            ): rescode.text
                        }
                    )
                    d.update(rescode.attrib.items())
                    d.update(product.attrib.items())
                    d.update(sub_product.attrib.items())
                    # print(d)
                    products.append(d)
    return products


def main():

    products = ReadProductXML(product_file)
    if db_not_exists:
        CreateNewDB()
    InsertIntoDB(db_file, products)


if __name__ == "__main__":
    main()
