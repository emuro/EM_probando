import pandas as pd


def test_df_local(df_local):
    df_aux = pd.DataFrame({"odd": [5, 7], "even": [6, 8]})
    df_local = pd.concat([df_local, df_aux], axis=0)
    df_local.reset_index(drop=True, inplace=True)
    print("local\n", df_local)
    return df_local

def test_list_local(list_local):
    list_aux = [5, 7]
    list_local = list_local + list_aux
    print("local\n", list_local)
    return list_local


def main():
    df_principal = pd.DataFrame({"odd": [1, 3], "even": [2, 4]})
    print("main-inicio:\n", "df_principal\n", df_principal)
    df_principal_cambiado = test_df_local(df_principal)
    print("main-afterLocal\ndf_principal\n", df_principal)
    print("main-afterLocal\ndf_principal_cambiado\n", df_principal_cambiado, "\n")

    list_principal = [1, 3]
    print("\n\nmain-inicio:\n", "list_principal\n", list_principal)
    list_principal_cambiado = test_list_local(list_principal)
    print("main-afterLocal\nlist_principal\n", list_principal)
    print("main-afterLocal\nlist_principal_cambiado\n", list_principal_cambiado, "\n")



if __name__ == "__main__":
    main()
