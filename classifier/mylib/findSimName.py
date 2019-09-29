
Simchar_list = ['凭', '莼', '宝', '彦', '凑', '况', '绣', '咸', '羡', '虬', '体', '机', '锈', '启', '叙', '炖', '禀', '绫', '万', '敌', '偻', '晋', '晒', '炉', '缙', '缇', '丑', '洒', '兹', '强', '丰', '响', '参', '缓', '鹊', '异', '碹', '宽', '厂', '锋', '嵛', '绚', '礼', '纯', '窃', '鸣', '冲', '党', '荐', '荣', '愿', '赋', '襁', '绒', '绮', '渊', '钧', '笋', '葱', '凉', '并', '双', '钿', '梦', '种', '莱', '献', '儿', '咨', '樱', '灯', '价', '阆', '虾', '嫒', '涌', '会', '复', '圣', '个', '扦', '柜', '洁', '么', '后', '适', '灵', '宁', '钦', '几', '尔', '愍', '只', '忏', '沓', '县', '荭', '表', '瑷', '札', '辟', '呵', '却', '联', '着', '污', '听', '岭', '制', '样', '静']
 
#find 名字是否含非繁體字會用之字的簡體字
def findSimName(name):
    for c in name:
        if c in Simchar_list:
            return True
    return False