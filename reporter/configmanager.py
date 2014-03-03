from xml.dom import minidom

class Config:
    query=""
    sqlitepath=""
    create_table = ""

def loadconfig(path = "config.xml"):
    config = Config()
    xmldoc = minidom.parse(path)

    for node in xmldoc.getElementsByTagName("sqlite"):
        config.sqlitepath = node.firstChild.nodeValue
        config.create_table = node.attributes["create_table"].value

    for node in xmldoc.getElementsByTagName("query"):
        config.query=node.firstChild.nodeValue
    return config