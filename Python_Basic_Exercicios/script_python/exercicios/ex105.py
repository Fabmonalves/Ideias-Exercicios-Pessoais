def notas(*num, sit =False):
    """_summary_
    Args:
        sit (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    boletim = dict()
    boletim["maior"] = max(num)
    boletim["menor"] = min(num)
    boletim["média"] = sum(num) / len(num)
    if sit == True:
        if boletim["média"] >= 7:
           boletim["situação"] = 'BOA'
        elif boletim["média"] >= 5:
            boletim["situação"] = 'REGULAR'
        else:
            boletim["situação"] = 'RUIM'
    return boletim
        


resp = notas(5, 2, 9, 10, 10, sit=True)
print(resp)
