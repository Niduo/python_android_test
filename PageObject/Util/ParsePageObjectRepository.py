from configparser import ConfigParser
from ProjectVar.var import page_object_repository_path#新加的
class ParsePageObjectRepositoryConfig(object):
    # def __init__(self,config_path):
    #     self.cf = ConfigParser() #生成解析器
    #     self.cf.read(config_path)
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(page_object_repository_path)

    def getItemSestion(self,sectionName):
        print(self.cf.items(sectionName))
        return dict(self.cf.items(sectionName))
    def getOptionValue(self,sectionName,optionName): #返回一个字典
        print(self.cf.get(sectionName,optionName))
        return self.cf.get(sectionName,optionName)
# if __name__=='__main__':
#     pp = ParsePageObjectRepositoryConfig()
#     # pp = ParsePageObjectRepositoryConfig("E:\\PYwork\\PageObject\\Conf\\PageObjectRepository.ini")
#     print(pp.getItemSestion("hoom_login"))
# print(pp.getOptionValue("hoom_login", "login_page.loginbutton"))