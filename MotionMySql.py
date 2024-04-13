import pymysql


class join:
    def join(self,host,user,password,library_name):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=library_name,
            cursorclass=pymysql.cursors.DictCursor,
        )
        self.cursor = self.conn.cursor()


class GetColumn:
    def GetColumn(self, cursor, conn, table_name):
        query = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'abc' AND TABLE_NAME = '{table_name}';"
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)
        column_names = [item["COLUMN_NAME"] for item in results]
        print(column_names)
        # ����һ���ֵ����洢�����Ͷ�Ӧ��ֵ
        column_values_dict = {}

        # ��ʾ�û�����ÿ�е�ֵ
        for column_name in column_names:
            while True:
                value = input(f"������{column_name}��ֵ��")
                if value:
                    column_values_dict[column_name] = value
                    break
                else:
                    print("���벻��Ϊ�գ�����������")

        # �������ֵ�������Ƿ����е�����ƥ��
        if len(column_values_dict) == len(column_names):
            # ������������INSERT��ѯ
            placeholders = ", ".join(["%s"] * len(column_names))
            insert_query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({placeholders})"
            print(insert_query)

            # ִ�в�������ѯ
            # cursor.execute(insert_query, list(column_values_dict.values()))
            try:
                cursor.execute(insert_query, list(column_values_dict.values()))
            except Exception as e:
                print(f"��������: {e}")
            conn.commit()
        else:
            print("�����ֵ���������е�������ƥ��")


class Inquire:
    def run(self, cursor, conn, table_name):
        try:
            # ��ȡ�û�����
            column_name = input("������Ҫ��ѯ������: ")
            search_term = input("������Ҫ�����Ĺؼ���: ")

            # ���ո��滻Ϊ`
            column_name = column_name.replace(" ", "`")
            search_term = search_term.replace(" ", "`")

            # ������ѯ���
            query = f"SELECT * FROM {table_name} WHERE `{column_name}` LIKE '%{search_term}%'"
            n = input("�Ƿ�ȷ�ϲ�������yes/no��")
            # ִ�в�ѯ
            if n == "yes":
                print("ȷ�ϲ���")
                cursor.execute(query)
                results = cursor.fetchall()

                # �����ѯ���
                if results:
                    for result in results:
                        print(result)
                    else:
                        print("û���ҵ��������!")
            else:
                print("ȡ������")

        except pymysql.Error as e:
            print(f"��ѯ����: {e}")
        except Exception as e:
            print(f"��������: {e}")


class delt:
    def deltf(self, cursor, conn, table_name):
        # ��ȡ�û�����
        column_name = input("������Ҫɾ��������: ")
        search_term = input("������Ҫɾ���Ĺؼ���: ")
        query = (
            f"SELECT * FROM {table_name} WHERE `{column_name}` LIKE '%{search_term}%'"
        )

        # ִ�в�ѯ
        cursor.execute(query)
        results = cursor.fetchall()

        # �����ѯ���
        if results:
            column_name = column_name.replace(" ", "`")
            search_term = search_term.replace(" ", "`")

            # ������ѯ���
            sql = f"DELETE FROM {table_name} WHERE `{column_name}` LIKE '%{search_term}%';"
            n = input("�Ƿ�ȷ�ϲ�������yes/no��")
            # ִ�в�ѯ
            if n == "yes":
                try:
                    # ִ��SQL���
                    cursor.execute(sql)
                    # �ύ�����ݿ�ִ��
                    conn.commit()
                    print("�ɹ�")
                except Exception as e:
                    # ��������ʱ�ع�
                    conn.rollback()
                    print(f"ִ��SQL����: {e}")
            else:
                print("ȡ������")
        else:
            print("û���ҵ��������!")


class Renewal:
    def Renewalf(self, cursor, conn, table_name):
        # ��ȡ�û�����
        column_name = input("����Ҫ���ĵ�����")  # ��ʵ�������滻
        search_term = input("����Ҫ��ѯ�Ĺؼ���")  # ��ʵ���������滻
        new_value = input("����Ҫ���ĵ�ֵ")  # ��ʵ�ʵ���ֵ�滻
        query = (
            f"SELECT * FROM {table_name} WHERE `{column_name}` LIKE '%{search_term}%'"
        )

        # ִ�в�ѯ
        cursor.execute(query)
        results = cursor.fetchall()

        # �����ѯ���
        if results:
            column_name = column_name.replace(" ", "`")
            search_term = search_term.replace(" ", "`")

            # ������ѯ���
            rwl = f"UPDATE {table_name} SET {column_name} = '{new_value}' WHERE {column_name} LIKE '%{search_term}%';"
            n = input("�Ƿ�ȷ�ϲ�������yes/no��")
            # ִ�в�ѯ
            if n == "yes":
                try:
                    # ִ��SQL���
                    cursor.execute(rwl)
                    # �ύ�����ݿ�ִ��
                    conn.commit()
                    print("�ɹ�")
                except Exception as e:
                    # ��������ʱ�ع�
                    self.conn.rollback()
                    print(f"ִ��SQL����: {e}")
        else:
            print("û���ҵ��������!")


def close(cursor, conn):
    cursor.close()  # �ر��α�
    conn.close()  # �ر�����