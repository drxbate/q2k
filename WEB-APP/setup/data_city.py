#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年8月11日

@author: ruixidong
'''
import sys
reload(sys)

setdefaultencoding = getattr(sys, "setdefaultencoding")

if setdefaultencoding:
    setdefaultencoding("utf8")
    
from DataAccess.Handler import RedisCli


data = u"""
001,上海
002,苏州
003,杭州
005,北京
007,重庆
008,成都
009,青岛
010,镇江
001001,徐汇
001002,普陀
001003,闸北
001004,虹口
001005,长宁
001006,杨浦
001007,静安
001008,黄浦
001009,卢湾
001011,浦东新
001012,嘉定
001013,宝山
001014,崇明
001015,松江
001016,金山
001017,青浦
001018,奉贤
001020,闵行
001021,川沙
002022,沧浪
002023,平江
002025,相城
002026,吴中
002027,高新
002028,工业园
002029,金阊
002081,昆山
003030,上城
003031,下城
003032,西湖
003033,拱墅
003034,江干
003035,滨江
003036,萧山
003037,余杭
003038,富阳市
004039,白下
005046,朝阳
005047,东城
005048,西城
005049,海淀
005050,石景山
005051,丰台
005052,宣武
005053,崇文
005054,大兴
005055,通州
005056,怀柔
005057,顺义
005058,昌平
005059,平谷
005060,房山
005061,门头沟
005062,密云县
005063,延庆县
005064,其它
006040,海曙
006041,江东
006042,江北
006043,鄞州
006044,北沦
006045,镇海
007065,渝中
007066,大渡口
007067,江北
007068,沙坪坝
007069,九龙坡
007070,南岸
007071,北碚
007072,万盛
007073,双桥
007074,渝北
007075,巴南
007076,万州
007077,涪陵
007078,长寿
007079,黔江
008080,市区
008089,市辖
008090,锦江
008091,青羊
008092,金牛
008093,武侯
008094,成华
008095,龙泉驿
008096,青白江
008097,新都
008098,温江县
008099,金堂县
008100,双流县
008101,郫县
008102,大邑县
008103,蒲江县
008104,新津县
008105,都江堰市
008106,彭州市
008107,邛崃市
008108,崇州市
008109,高新
008115,华阳
009082,市南
009083,市北
009084,崂山
009085,城阳
009086,四方
009087,李沧
009088,青岛开发
009110,即墨市
009111,胶南市
009112,胶州市
009113,莱西市
009114,平度市
010116,京口
010117,润州
010118,丹徒
001007017,静安寺                                  
001007018,南京西路                                
001007019,北京西路                                
001008030,南京东路                                
001008031,豫园                                    
001008032,人民广场                                
001008033,外滩                                    
001008034,蓬莱公园                                
001009020,淮海中路                                
001009021,打浦路                                  
001009022,新天地                                  
001009023,鲁班路斜土                              
001009634,复兴中路                                
001011035,陆家嘴                                  
001011036,世纪公园                                
001011037,金桥                                    
001011038,张江                                    
001011039,八佰伴                                  
001011040,世博会                                  
001011041,塘桥                                    
001011042,三林                                    
001011485,源深洋泾                                
001011486,东城                                    
001011487,北蔡                                    
001011488,大三林                                  
001011489,金杨                                    
001011490,碧云                                    
001011491,曹路                                    
001011492,川沙                                    
001011493,高桥                                    
001011494,高行                                    
001011993,竹园
001012055,嘉定老城                                
001012510,安亭                                    
001012511,南翔                                    
001012512,丰庄                                    
001012513,江桥                                    
001013056,大华                                    
001013057,新城                                    
001013058,沪太路                                  
001013059,上海大学                                
001015496,九亭                                    
001015497,新桥                                    
001015498,泗泾                                    
001015499,佘山                                    
001015500,松江新城                                
001016514,朱泾镇                                  
001016515,石化                                    
001016516,枫泾                                    
001016517,金山新城开                              
001016518,金山其它板                              
001017519,青浦新城                                
001017520,重固                                    
001017521,白鹤                                    
001017522,徐泾                                    
001017523,赵巷                                    
001017524,朱家角                                  
001017525,华新镇                                  
001017526,练塘镇                                  
001017527,金泽镇                                  
001020001,七宝                                    
001020002,莘庄                                    
001020003,龙柏金汇
001020004,漕宝路
001020005,古美罗阳
001020528,老闵行
001020529,颛桥
001020530,春申
001020531,古北
001020532,虹桥静安新城                            
001020533,华漕                                    
001020534,马桥                                    
001020535,吴泾                                    
001020536,浦江                                    
002022701,干将东路
002022702,西环路
002022703,十全街
002022704,三香路
002022705,干将西路
002022706,沧浪新城
002023707,观前街
002023708,平江新城
002025712,相城大道
002025720,阳澄湖
002026721,通园路
002026722,车坊
002026724,通达路
002026725,郭巷
002026726,东吴北路
002026727,甪直
002026728,木渎
002026729,石湖                                  
002026730,太湖                                    
002027718,玉山路
002027719,滨河路
002027723,塔园路
002027732,狮山路
002027733,竹园路
002027734,浒关
002027735,虎丘                           
002027736,长江路                                
002027737,何山路                                  
002028738,金湖湾商业街
002028739,湖畔天城商业街
002028740,新街口商业街
002028741,唯亭                            
002028742,娄葑
002028743,星湖街                                  
002028744,圆融时代广场
002028745,雅戈尔雷迪森广场
002028746,现代大道东
002028747,苏胜路
002028748,湖左岸商业街
002028749,白塘生态植物园
002028750,湖滨大道
002028751,馨都广场
002028967,金鸡湖大道
002028968,东城世纪广场
002028969,星都广场
002028970,中央公园
002028971,师惠坊商业街
002028972,园区世纪广场
002028973,跨塘镇商业街
002028974,斜塘联丰商业广场
002028975,现代大道西
002028976,方洲邻里中心
002028977,独墅湖高教区
002028978,贵都邻里中心
002028979,湖东邻里中心
002028980,中天湖畔广场
002028981,玲珑邻里中心
002028982,青剑湖商业广场
002028983,胜浦镇商业街
002028984,新城邻里中心
002028985,沙湖生态公园
002029752,金闾新城
002029756,石路街道
002081757,昆山市
003030328,湖滨                                    
003030329,清波                                    
003030330,紫阳                                    
003030331,望江                                    
003030332,南星                                    
003030333,小营                                    
003030637,近江                                    
003030638,复兴                                    
003031334,天水                                    
003031335,武林                                    
003031336,长庆                                    
003031337,潮鸣                                    
003031338,朝晖                                    
003031339,文晖                                    
003031340,东新                                    
003031341,石桥                                    
003032342,北山                                    
003032343,西溪                                    
003032344,灵隐                                    
003032345,翠苑                                    
003032346,文新                                    
003032347,古荡                                    
003032639,之江                                    
003033348,上塘                                    
003033349,米市巷                                  
003033350,湖墅                                    
003033351,小河                                    
003033352,拱宸桥                                  
003033353,和睦                                    
003033354,大关街                                  
003033355,康桥                                    
003033356,半山                                    
003034357,闸弄口                                  
003034358,凯旋                                    
003034359,采荷                                    
003034360,四季青                                  
003034635,钱江新城                                
003034636,三里亭                                  
003035361,西兴                                    
003035362,中兴                                    
003035363,之江                                    
003035364,长河                                    
003035365,浦沿                                    
003035366,东冠                                    
003036371,东冠                                    
003036372,北干                                    
003036373,城厢                                    
003036374,新塘                                    
003036375,新湾                                    
003036376,河庄                                    
003036377,南阳                                    
003036378,宁围                                    
003036379,文堰                                    
003036380,所前                                    
003036381,进化                                    
003036382,戴村                                    
003037367,临平                                    
003037368,南苑                                    
003037369,东湖                                    
003037370,星桥                                    
003037543,钱江新城                                
003037544,三里亭                                  
003037545,申花                                    
003037546,留下                                    
003037547,余杭                                    
003037548,拱墅                                    
003037549,嘉绿                                    
003037550,闲林                                    
003037551,求是                                    
003037552,古翠                                    
003037553,丰潭                                    
003037554,紫金                                    
005046095,建国门                                  
005046096,三里屯                                  
005046097,团结湖                                  
005046098,左家庄                                  
005046099,燕莎                                    
005046100,国展                                    
005046101,望京                                    
005046102,雅宝路                                  
005046103,劲松                                    
005046104,化工大学                                
005046105,中日医院                                
005046106,亚运村                                  
005046107,麦子店                                  
005046108,朝阳公园                                
005046109,酒仙桥                                  
005046110,北沙滩                                  
005046111,八王坟                                  
005046112,安贞                                    
005046113,西坝河                                  
005046114,延静里                                  
005046115,静安庄                                  
005046116,芍药居                                  
005046117,国贸                                    
005046118,京广                                    
005046119,三元桥                                  
005046120,红庙                                    
005046121,定福庄                                  
005046122,管庄                                    
005046123,双井                                    
005046124,潘家园                                  
005046125,东大桥                                  
005046126,光熙门                                  
005046127,十里堡                                  
005046128,八里庄                                  
005046625,CBD                                     
005046626,百子湾                                  
005046627,朝阳                               
005046628,东直门                                  
005046629,工体                                    
005046630,国贸                                    
005046631,三里                                  
005046632,双井                                    
005047129,王府井                                  
005047130,灯市口                                  
005047131,东四十条                                
005047132,东直门                                  
005047133,和平里                                  
005047134,地坛                                    
005047135,安定门                                  
005047136,金宝街                                  
005047137,雍和宫                                  
005047138,东外大街                                
005047139,雅宝路                                  
005047140,东中街                                  
005048141,复兴门                                  
005048142,阜城门                                  
005048143,西单                                    
005048144,钓鱼台                                  
005048145,小西天                                  
005048146,木樨地                                  
005048147,西直门                                  
005048148,德胜门                                  
005048149,三里河                                  
005048150,月坛                                    
005048151,金融街                                  
005048152,六铺炕                                  
005048153,北营房                                  
005048154,积水潭                                  
005048155,白云路                                  
005049062,海淀                                    
005049063,公主坟                                  
005049064,万寿路                                  
005049065,北京大学                                
005049066,双愉树                                  
005049067,中关村                                  
005049068,北太平庄                                
005049069,魏公村                                  
005049070,小南庄                                  
005049071,知春路                                  
005049072,车道沟                                  
005049073,上地                                    
005049074,三义庙                                  
005049075,百万庄                                  
005049076,圆明园                                  
005049077,甘家口                                  
005049078,农大                                    
005049079,海淀黄庄                                
005049080,大钟寺                                  
005049081,五道口                                  
005049082,学院路                                  
005049083,蓟门桥                                  
005049084,航天桥                                  
005049085,二里庄                                  
005049086,罗庄东里                                
005049087,紫竹园                                  
005049088,西八里庄                                
005049089,万泉寺                                  
005049090,牡丹园                                  
005049091,马甸                                    
005049092,紫竹桥                                  
005049093,北沙滩                                  
005049094,定慧寺                                  
005050198,古城                                    
005050199,苹果园                                  
005050200,八角                                    
005050201,老山                                    
005050202,鲁谷                                    
005050203,杨庄                                    
005050204,晋元庄                                  
005050205,玉泉路                                  
005050206,模式口                                  
005051175,方庄                                    
005051176,西罗园                                  
005051177,六里桥                                  
005051178,洋桥                                    
005051179,西客站                                  
005051180,角门                                    
005051181,木樨园                                  
005051182,赵公口                                  
005051183,成寿寺                                  
005051184,大红门                                  
005051185,西局                                    
005051186,北大地                                  
005051187,丰益桥                                  
005051188,世界公园                                
005051189,科技园区                                
005051190,卢沟桥                                  
005051191,马家堡                                  
005051192,刘家窑                                  
005051193,小瓦窑                                  
005051194,菜户营                                  
005051195,太平桥                                  
005051196,开阳里                                  
005051197,万柳桥                                  
005052162,长椿街                                  
005052163,广安门                                  
005052164,陶然亭                                  
005052165,天宁寺                                  
005052166,白纸坊                                  
005052167,南菜园                                  
005052168,枣林前街                                
005052169,天伦北里                                
005052170,右安门                                  
005052171,双槐里                                  
005052172,马连道                                  
005052173,牛街                                    
005052174,虎坊桥                                  
005053156,东花市                                  
005053157,崇文门                                  
005053158,幸福大街                                
005053159,光明楼                                  
005053160,天坛                                    
005053161,沙子口                                  
005054230,西红门                                  
005054231,兴华园                                  
005054232,黄村                                    
005054233,上清园                                  
005055213,西上园                                  
005055214,物资学院                                
005055215,梨园                                    
005055216,北苑                                    
005055217,土桥                                    
005055218,新华大街                                
005055219,新华联                                  
005055220,果园                                    
005057221,樱花园                                  
005057222,建新北区                                
005057223,石门苑                                  
005058224,立水桥                                  
005058225,小汤山                                  
005058226,回龙观                                  
005058227,天通苑                                  
005060207,窦店                                    
005060208,琉璃河                                  
005060209,行宫园                                  
005060210,良乡                                    
005061211,大峪                                    
005061212,双峪                                    
005063228,八达岭                                  
005063229,张山营                                  
007065234,解放杯CBD                               
007065235,上清寺行政                              
007065236,两路口                                  
007065237,大坪                                    
007065238,菜元黄沙溪                              
007065239,鹅岭                                    
007065240,国际村                                  
007065241,七星岗                                  
007065242,朝天门                                  
007066314,马王乡                                  
007066315,新山村                                  
007066316,九宫庙                                  
007066317,陶瓷市场                                
007066318,政府广场                                
007066319,茄子溪                                  
007066320,跃进村                                  
007067243,五黄路                                  
007067244,观音桥                                  
007067245,北城步行街                              
007067246,石门南桥寺                              
007067247,华新董家溪                              
007067248,人和镇北部                              
007067249,红旗河沟                                
007067250,铁山坪森林                              
007067251,五里店                                  
007067252,黄泥塝                                  
007067253,龙溪镇                                  
007067254,北城天街                                
007067255,海关                                    
007067256,松树桥                                  
007068280,三峡广场                                
007068281,土湾                                    
007068282,凤天路                                  
007068283,双碑磁器口                              
007068284,杨公桥                                  
007068285,小龙坎                                  
007068286,平顶山                                  
007068287,联芳十小路                              
007068288,重大科技园                              
007068289,学府路                                  
007068290,烈士墓                                  
007068291,新桥                                    
007068292,高滩岩                                  
007068293,覃家岗                                  
007068294,天星桥                                  
007069295,杨家坪                                  
007069296,高新区                                  
007069297,巴山                                    
007069298,二郎                                    
007069299,华岩                                    
007069300,上桥                                    
007069301,中粱山                                  
007069302,陈家坪                                  
007069303,石坪桥                                  
007069304,走马经济园                              
007069305,袁家岗                                  
007069306,西彭                                    
007069307,高庙科技新                              
007069308,谢家湾                                  
007069309,马家岩                                  
007069310,石桥铺                                  
007069311,新桥                                    
007069312,黄桷坪                                  
007069313,含谷开发区                              
007070265,弹子石                                  
007070266,海棠溪                                  
007070267,南坪转盘步                              
007070268,经济技术开                              
007070269,回龙工业园                              
007070270,四公里                                  
007070271,铜元局                                  
007070272,海峡路                                  
007070273,龙职中                                  
007070274,经开区                                  
007070275,南坪东路                                
007070276,区委                                    
007070277,南山                                    
007070278,茶园新区                                
007070279,南滨路                                  
007071321,城西新区                                
007071322,北碚井口                                
007071323,同兴                                    
007074257,两路空港                                
007074258,加洲新牌坊                              
007074259,回兴经开科                              
007074260,龙溪花卉                                
007074261,加洲                                    
007074262,新牌坊                                  
007074263,冉家坝                                  
007074264,渝北回兴                                
007075324,李家沱                                  
007075325,大江工业园                              
007075326,一品镇圣灯                              
007075327,鱼洞                                    
008090832,滨江路
008090833,成仁路
008090834,川师
008090835,春熙路
008090836,海椒市
008090837,红星路
008090838,九眼桥
008090839,莲桂路
008090840,龙舟路
008090841,牛市口
008090842,牛王庙
008090843,盐市口
008090844,合江亭
008090845,水碾河
008090846,静居寺
008090847,锦江周边
008091812,八宝街
008091813,百花中心站
008091814,贝森
008091815,长顺街
008091816,草市街
008091817,杜甫草堂
008091818,府南新区
008091819,浣花小区
008091820,光华
008091821,浣花小区
008091822,金沙
008091823,青羊小区
008091824,顺城街
008091825,天府广场
008091826,西南财大
008091827,太升路
008091828,外光华
008091829,铁门坎
008091830,内光华
008091831,青羊周边
008092848,茶店子
008092849,抚琴小区
008092850,荷花池
008092851,花牌坊
008092852,黄忠
008092853,交大路
008092854,九里堤
008092855,李家沱
008092856,马鞍路
008092857,沙湾会展
008092858,蜀汉路
008092859,营门口
008092860,昭觉寺
008092861,曹家巷
008092862,三友路
008092863,火车北站
008092864,梁家巷
008092865,驷马桥
008092866,金牛周边
008093792,高升桥
008093793,航空路
008093794,红牌楼
008093795,火车南站
008093796,磨子桥
008093797,内双楠
008093798,清水河
008093799,人民南路
008093800,跳伞塔
008093801,桐梓林
008093802,武侯祠大街
008093803,外双楠
008093804,玉林
008093805,望江路
008093806,肖家河
008093807,晋阳街
008093808,五大花园
008093809,小天竺街
008093810,金花镇
008093811,武侯周边
008093963,九茹村
008093964,紫荆
008093965,林荫街
008093966,科华北路
008094867,八里小区
008094868,电子科大
008094869,建设路
008094870,猛追湾
008094871,十里店
008094872,双桥子
008094873,万年场
008094874,新鸿路
008094875,新华公园
008094876,玉双路
008094877,府青路
008094878,青龙场
008094879,龙潭寺
008094880,五桂桥
008094881,二仙桥
008094882,成华周边
008109883,芳草街
008109884,南沿线
008109885,神仙树
008109886,肖家河
008109887,紫荆
008109888,中和镇
009082791,福州南路
009082889,八大湖 
009082890,八大关
009082891,巴黎春天
009082892,东海路
009082893,大学路
009082894,二轻新村
009082895,浮山所
009082896,广电大厦
009082897,火车站
009082898,青岛大学
009082899,五四广场
009082900,西镇 
009082901,辛家庄
009082902,湛山 
009082903,中山路
009083904,错埠岭
009083905,大港
009083906,浮山后
009083907,海泊桥
009083908,华阳路
009083909,即墨路
009083910,辽宁路
009083911,啤酒街 
009083912,市北家乐福
009083913,台东 
009083914,杨家群
009084936,高科园
009084937,海尔路
009084938,姜哥庄
009084939,崂山区政府
009084940,李山东路
009084941,麦岛
009084942,青岛二中
009084943,沙子口
009084944,山东头
009084945,石老人
009084946,松岭路
009084947,王家村
009084948,颐中体育场 
009085949,流亭
009085950,夏庄
009085951,惜福镇
009085952,正阳路 
009086915,北岭
009086916,长途站 
009086917,抚顺路
009086918,海琴广场
009086919,海云庵
009086920,河西
009086921,理工大学
009086922,南宁路
009086923,水清沟 
009086924,双山
009086925,兴隆路
009087926,沧口公园
009087927,河南庄
009087928,黑龙江路
009087929,金水路
009087930,李村公园
009087931,楼山路
009087932,十梅庵
009087933,书院路
009087934,下王埠
009087935,振华路 
009088953,保税区
009088954,长江路
009088955,黄岛
009088956,香江路
009088957,薛家岛
009110958,即墨市
009111959,胶南市
009112960,胶州市
009113961,莱西市
009114962,平度市
001001006,徐汇中心                                
001001007,田林                                    
001001008,梅陇                                    
001001009,龙华                                    
001001010,万体馆                                  
001001633,复兴中路                                
001001986,淮海中路
001001987,乌鲁木齐路
001001988,陕西南路
001001989,建国西路
001001990,衡山路
001001991,湖南路
001001992,大木桥
001002049,曹杨长风                                
001002050,武宁长寿                                
001002051,石泉宜川                                
001002053,真北真南真                              
001002054,长寿路亚新                              
001002501,宜川                                    
001002502,桃浦                                    
001002503,真如                                    
001002504,长寿路                                  
001002505,武宁                                    
001002506,万里                                    
001002507,曹杨                                    
001002508,长风                                    
001002509,长征                                    
001003047,彭浦                                    
001003048,原平路                                  
001003052,大宁                                    
001003994,上海火车站
001003995,不夜城
001003996,中山北路
001003997,西藏北路
001003998,七浦路
001004025,曲阳                                    
001004026,凉城                                    
001004027,四川北路                                
001004028,提篮桥                                  
001004029,虹口公园                                
001005011,中山公园                                
001005012,古北                                    
001005013,虹桥                                    
001005014,北新泾                                  
001005015,天山仙霞                                
001005495,新华路                                  
001006043,五角场                                  
001006044,中原                                    
001006045,控江                                    
001006046,鞍山                                    
001006542,新江湾城                                
001007016,曹家渡                                  
002028999,天虹百货
002028a00,左岸商业街
002028a01,星州街
002028a02,高和路
002028a03,湖畔商圈
002027a04,珠江路
002027a05,金枫路
002027a06,汾湖路

"""

if __name__=="__main__":
    for k in RedisCli.keys("metadata:district:*"):
        RedisCli.delete(k)

    for i in data.split("\n"):
        if i=="":
            continue
        cd,name=i.split(",",2)
        if len(cd)==3:
            RedisCli.set("metadata:district:%s"%cd,name.encode("utf8"))
        elif len(cd)==6:
            RedisCli.set("metadata:district:%s:%s"%(cd[:3],cd[3:]),name.encode("utf8"))
        elif len(cd)==9:
            RedisCli.set("metadata:district:%s:%s:%s"%(cd[:3],cd[3:6],cd[6:]), name.encode("utf8"))
            
    