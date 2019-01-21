#coding:utf-8
import yaml
class OperateYaml:
    def __init__(self,file=None):
        if file:
            self.file = file
        else:
            self.file =r"C:\zixueautojiaoben\pmi\AccountOpen.yml"
        self.yaml_data = self.read_yaml()

    def read_yaml(self):
        with open(self.file,"r") as fp:
            data = yaml.load(fp)
        return data

    def get_id(self,name,key):
        sequence_id = self.yaml_data[name][key]
        return sequence_id
    def serial_id(self,id):
        info1 = {"serial":{"serial":id}}
        return info1
    def write_serial_id(self,id):
        data = self.serial_id(id)
        with open(self.file,"w") as fp:
            yaml.dump(data,fp,allow_unicode=True)
        fp.close()
    def sign_id(self,id):
        info2 = {"sign":id}
        return info2
    def write_sign_id(self,id):
        data = self.sign_id(id)
        with open(self.file,"a") as fp:
            yaml.dump(data,fp,allow_unicode=True)
        fp.close()

    def exchange_token_id(self, id):
            info2 = {"exchange_token": id}
            return info2

    def write_exchange_token_id(self, id):
            data = self.exchange_token_id(id)
            with open(self.file, "a") as fp:
                yaml.dump(data, fp, allow_unicode=True)
            fp.close()

    def agreement_no_id(self, id):
        info2 = {"agreement_no": id}
        return info2

    def write_agreement_no_id(self, id):
        data = self.agreement_no_id(id)
        with open(self.file, "a") as fp:
            yaml.dump(data, fp, allow_unicode=True)
        fp.close()
    #def create_sequence_id(self,id):
       # info1 = {"order_no":id}
        #return info1



#if __name__ == '__main__':