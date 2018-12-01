import urllib2
import urllib
import requests
import os
import time
import cookielib
from lxml import html
loginUrl = 'http://www.zhihu.com/api/v3/oauth/sign_in'
send_headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-length': '400',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'tgw_l7_route=bc9380c810e0cf40598c1a7b1459f027; _zap=8d681745-c33e-4636-9320-1f57d22f4caf; _xsrf=svLsxpd45Rh82DSrsANWWYdQncxEd1q9; d_c0="ALAguPG2mg6PTuK4AP12TJZlgG6I52eEbzg=|1543680891"; capsion_ticket="2|1:0|10:1543680893|14:capsion_ticket|44:YWY3NjNlMzgyYmFhNGQzNWI5OTc3ZWM5NzUwNzU0NGE=|f59a008972be0ac306563622f9bed34c4fd609c7c0cc6d8891fe64306a3cdfc5"',
    'origin': 'https://www.zhihu.com',
    'pragma': 'no-cache',
    'referer': 'https://www.zhihu.com/signup?next=%2F',
    'user-agent': 'Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Raspbian Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36',
    'x-ab-param': 'top_bill=0;top_quality=0;top_v_album=1;top_ntr=1;top_alt=0;top_raf=n;top_recall_core_interest=81;top_yhgc=0;top_adpar=0;pf_creator_card=0;top_no_weighing=1;top_scaled_score=0;se_filter=0;top_recall_deep_user=1;se_cq=1;se_time_search=origin;top_newfollow=0;top_universalebook=1;top_user_gift=0;top_billpic=0;top_gr_auto_model=0;top_tagore=1;top_tagore_topic=0;se_billboard=3;top_billvideo=0;top_newfollowans=0;top_rank=0;top_local=1;top_memberfree=1;top_recall_tb_follow=71;se_wiki_box=1;top_vd_op=0;se_tf=1;top_followtop=1;tp_discussion_feed_card_type=0;top_login_card=1;top_card=-1;top_root_mg=1;top_yc=0;pin_efs=orig;top_hweb=0;top_promo=1;top_ab_validate=0;top_hqt=0;top_retag=0;se_sltr=0;top_lowup=1;se_majorob_style=0;top_nad=1;top_pfq=0;se_product_rank_list=0;top_video_score=1;ls_new_video=0;se_dl=1;top_30=0;top_manual_tag=1;se_billboardsearch=0;top_is_gr=0;top_recall_tb_long=51;se_qc=0;se_websearch=0;top_feedre_cpt=101;top_test_4_liguangyi=1;top_deep_promo=0;top_roundtable=1;top_topic_feedre=21;top_ebook=0;top_video_rew=0;top_wonderful=1;top_vds_alb_pos=0;top_vdio_rew=0;top_videos_priority=-1;top_ad_slot=1;top_root_ac=1;top_feedre_rtt=41;top_tmt=0;se_ltr=1;se_new_market_search=off;top_nucc=0;top_cc_at=1;top_rerank_isolation=-1;se_backsearch=0;top_fqa=0;top_recall_tb=1;top_tuner_refactor=-1;top_video_fix_position=0;top_an=0;top_retagg=0;tp_ios_topic_write_pin_guide=1;pin_ef=orig;top_billboard_count=1;top_nid=0;se_rescore=1;se_gi=0;top_uit=0;top_nszt=0;se_major_onebox=major;top_recall_follow_user=91;top_gr_model=0;se_minor_onebox=d;se_merger=1;top_gif=0;top_tr=0;se_dt=1;top_mt=0;top_rerank_breakin=-1;zr_ans_rec=gbrank;top_fqai=0;se_consulting_price=n;top_new_user_gift=0;top_feedtopiccard=0;top_rerank_reweight=-1;top_slot_ad_pos=1;top_ac_merge=0;top_follow_reason=0;top_new_feed=1;top_nuc=0;top_recall=1;top_vd_gender=0;top_feedre_itemcf=31;top_f_r_nb=1;ls_new_score=0;top_free_content=-1;tp_discussion_feed_type_android=0;se_gemini_service=content;top_recommend_topic_card=0;top_sj=2;top_tffrt=0;tp_write_pin_guide=3;se_ad_index=10;top_billupdate1=2;ls_is_use_zrec=0;top_hca=0;top_multi_model=0;top_spec_promo=1;tp_favsku=a;top_billread=1;top_root_few_topic=0;se_ingress=on;top_billab=0;top_mlt_model=0;top_sjre=0;se_correct_ab=0;se_relevant_query=new;top_rerank_repos=-1;top_recall_tb_short=61;top_root_web=0;tp_sft=a;se_consulting_switch=off;top_gr_topic_reweight=0;top_root=0;se_entity=on;se_auto_syn=0;top_distinction=0;top_dtmt=2;top_feedre=1;top_tag_isolation=0;se_cm=1;se_daxuechuisou=new;se_engine=0;se_refactored_search_index=0;top_nmt=0;top_vd_rt_int=0',
    'x-requested-with': 'fetch',
    'x-udid': 'ALAguPG2mg6PTuK4AP12TJZlgG6I52eEbzg=',
    'x-xsrftoken': 'svLsxpd45Rh82DSrsANWWYdQncxEd1q9',
    'x-zse-83': '3_1.1'
}
logindata = 'kpuy6HdpNsav8hv2ulRvHPs2Qgbf02uwhtuzJddpNsav8hv2ulRvAL01QgbfIlepisMxI6dzQgbfclrhw6QwO0sw8xNa098l-obus0uoclbf9hRzmlR1609lMsq_Sk8k_1rlRC_mLwr_ahrljsapNKpxHdQtMtQ1kx8k0_oxRsua8xekw2rwM9_m7lbvOs8lj_rwPC0wLgAu6lNkw08xNOox0pr4Nsqxjtf262PxDlRbMs7w12BjPdtyCDRdHXQwXlrh0D01PXAqQgrhl1NlNGomK5NbNorlgoOk09sz6pBq0Puylx8k0O01J2BqNde1Xlrh00s3OXtrIdA13x8k095k0-NbLkrxgcAl0-owNgu_Albl-crwQWKwRwev8lNwXlrh9-PvOTevDLQw: '
#cookie保存的文件名
filename='cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie
cookie=cookielib.MozillaCookieJar(filename)
#创建opener用于读取Url
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
opener.addheaders = send_headers
#模拟登录
postdata=urllib.urlencode(logindata)
#登录
result=opener.open(loginUrl,postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址
gradeUrl="http://www.zhihu.com"
result=opener.open(gradeUrl)
print result.read()