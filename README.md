# 109年 Aigo AI智慧應用新世代人才培育計畫．人才解題 數據分析組 

<p align="center">
  <img width="200" height="200" src="https://github.com/chikangtsai/Aigo-hai1uD/blob/main/海陸package/gloden陸.jpg">
</p>

<h2>TOPIC: AIOT智慧用量偵測與異常警示系統</h2><br/>

<h2>解題團隊：大安紅蠍隊</h2><br/>

<h2>出題企業：海陸家赫</h2><br/>
<h3>解題內容摘要 ：<h3><br/><br/>
  海陸家赫公司希望能將服務力轉化為業務力，讓公司與顧客間的關係更為緊密，要做到這件事我們必須
  了解1.顧客需要什麼？2.顧客何時需要？接著統整以上資訊，導入自動化客服機器人，幫助提供最即時
  且精準的商品推薦，積極把握潛在訂單，提升顧客忠誠度。 
  目前海陸家赫是以 RFM 模型來進行客戶分類，而我們探討相關domain knowledge 之後，將結合 RFM
  模型以及顧客活躍度(Customer Active Index, CAI)指標，幫助公司針對不同的顧客做出不同的商品
  推薦，了解顧客需要什麼。 
  知道顧客需要什麼之後，下一步就是要知道顧客何時需要。針對這部分，我們以 AI 方法進行建模，從
  客戶過往累積的消費行為及模式中發掘數據價值，以 XGBoost 、LSTM模型來預估顧客的下一次購買時
  點，進而做到在正確的時間做出正確的推薦，同時整合自動化客服機器人，即時進行商品推薦及需求回
  應，提升顧客之消費體驗滿意度及品牌忠誠度。 <br/><br/>
  
<h3>解題成果簡述  ：<h3><br/><br/>
  相較於原本企業內部的(平均方法)，本次計畫提升下一次購買時點之預測精準度。<br/>
  該公司將業務依金額分為：A(最高金額)、B、C、D(最少金額)級 <br/>
  A 類訂單，海陸家赫公司原本的預測方法誤差為 241.7天，而我們的預測誤差僅 6.7天，精準度提升97% <br/>
  B 類訂單，海陸家赫公司原本的預測方法誤差為 227.6天，而我們的預測誤差僅11.4天，精準度提升94% <br/>
  C 類訂單，海陸家赫公司原本的預測方法誤差為190.7天，而我們的預測誤差僅22.5天，精準度提升88% <br/>
  D 類訂單，海陸家赫公司原本的預測方法誤差為 246.4天，而我們的預測誤差僅49.5天，精準度提升79% <br/><br/>

  1.  以 RFM 模型結合 CAI 指標，根據不同客戶特性進行商品推薦 <br/>
  2.  打造 line@自動化客服機器人，根據 RFM 及 CAI 之計算結果主動進行商品推薦，並快速回應顧客需求，提升顧客之消費體驗滿意度及品牌忠誠度 <br/><br/>

<h3>此份package 包含：<h3><br/>
1）資料整理、視覺化<br/><br/>  2) RFM產品推薦<br/><br/>  3) xgboost預測<br/><br/>   4) LSTM預測<br/><br/>  5) Line-bot測試用程式碼<br/><br/>
#由於資料保密協議僅留有一檔案保留測試紀錄

<h3>參考： Line bot Q-Code<h3>

<p align="center">
  <img width="200" height="200" src="https://github.com/chikangtsai/Aigo-hai1uD/blob/main/海陸package/QRCODE.PNG">
</p>

<h3>參考文獻 <h3><br/>
Abbasimehr,  H.,  Shabani,  M.,  & Yousefi,  M.  (2020). An  optimized  model  using 
LSTM network for demand forecasting. Computers & Industrial Engineering, 
143, 13. doi:10.1016/j.cie.2020.106435 
Babak Sohrabi, K. A. (2007). Customer lifetime value (CLV) measurement based on 
RFM model.  
Bitewulign KassaMekonnen, W. b., Tung-Han Hsieh, Shien-Kuei Liaw, Fu-Liang 
Yang. (2020). Accurate prediction of glucose concentration and identification 
of  major  contributing  features  from  hardly  distinguishable  near-infrared 
spectroscopy. 59.  
Cao, K., Kim, H., Hwang, C., & Jung, H. (2018). CNN-LSTM Coupled Model for 
Prediction  of  Waterworks  Operation.  Journal  of  Information  Processing 
Systems, 14(6), 1508-1520. doi:10.3745/jips.02.0104 
Carbery,  C.  M.,  Woods,  R.,  &  Marshall,  A.  H.  (2019).  A  new  data  analytics 
framework  emphasising  preprocessing  of  data  to  generate  insights  into 
complex manufacturing systems. Proceedings of the Institution of Mechanical 
Engineers Part C-Journal of Mechanical Engineering Science, 233(19-20), 
6713-6726. doi:10.1177/0954406219866867 
Ching-Hsue Cheng, Y.-S. C. (2009). Classifying the segmentation of customer value 
via RFM model and RS theory. ELSEVIER, 36(3), 4176-4184.  
Choi, D.-K. (2019). Data-Driven Materials Modeling with XGBoost Algorithm and 
Statistical  Infer-ence Analysis  for  Prediction  of  Fatigue  Strength  of  Steels.  
International Journal of Precision Engineering and Manufacturing, 129-138.  
Dong, W., Huang, Y. M., Lehane, B., & Ma, G. W. (2020). XGBoost algorithm-based 
prediction of concrete electrical resistivity for structural health monitoring. 
Automation in Construction, 114, 11. doi:10.1016/j.autcon.2020.103155 
Fader, P. S., Hardie, B. G. S., & Lee, K. L. (2005). RFM and CLV: Using iso-value 
curves for customer base analysis. Journal of Marketing Research, 42(4), 415-
430. doi:10.1509/jmkr.2005.42.4.415 
Farrugia, S., Ellul, J., & Azzopardi, G. (2020). Detection of illicit accounts over the 
Ethereum  blockchain.  Expert  Systems  with  Applications,  150,  11. 
doi:10.1016/j.eswa.2020.113318 
Gertz,  M.,  Grosse-Butenuth,  K.,  Junge,  W.,  Maassen-Francke,  B.,  Renner,  C., 
Sparenberg, H., & Krieter, J. (2020). Using the XGBoost algorithm to classify 
neck  and  leg  activity  sensor  data  using  on-farm  health  recordings  for 
locomotor-associated  diseases.  Computers  and  Electronics  in  Agriculture, 
173, 10. doi:10.1016/j.compag.2020.105404 
Guo, J. Y., Xie, Z., Qin, Y., Jia, L. M., & Wang, Y. G. (2019). Short-Term Abnormal 
Passenger  Flow Prediction Based on  the Fusion of SVR and  LSTM.  IEEE 
ACCESS, 7, 42946-42955. doi:10.1109/access.2019.2907739 
Han, Z. Z., Shang, M. Y., Liu, Z. B., Vong, C. M., Liu, Y. S., Zwicker, M., . . . Chen, 
C.  L.  P.  (2019).  SeqViews2SeqLabels:  Learning  3D  Global  Features  via 
Aggregating Sequential Views by RNN With Attention. Ieee Transactions on 
Image Processing, 28(2), 658-672. doi:10.1109/tip.2018.2868426   
Hochreiter, B., Frasconi, & Schmidhuber. (2001). Gradient Flow in Recurrent Nets: 
the Difficulty of Learning Long-Term Dependencies.  
Ji,  X.  J.,  Tong,  W.  D.,  Liu,  Z.  C.,  &  Shi,  T.  L.  (2019).  Five-Feature  Model  for 
Developing the Classifier for Synergistic vs. Antagonistic Drug Combinations 
Built  by  XGBoost.  Frontiers  in  Genetics,  10,  13. 
doi:10.3389/fgene.2019.00600 
Le Thi Le, H. N., Jian Zhou, Jie Dou  and Hossein Moayedi. (2019). Estimating the 
Heating Load of Buildings for Smart City Planning Using a Nov-el Artificial 
Intelligence Technique PSO-XGBoost.  
Lei, X. Y., Pan, H. G., & Huang, X. D. (2019). A Dilated CNN Model for Image 
Classification.  IEEE  ACCESS,  7,  124087-124095. 
doi:10.1109/access.2019.2927169 
Li, Y., Liu, D., Li, H. Q., Li, L., Li, Z., & Wu, F. (2019). Learning a Convolutional 
Neural Network for Image Compact-Resolution. Ieee Transactions on Image 
Processing, 28(3), 1092-1107. doi:10.1109/tip.2018.2872876 
Lu, H. F., & Ma, X. (2020). Hybrid decision tree-based machine learning models for 
short-term  water  quality  prediction.  Chemosphere,  249,  12. 
doi:10.1016/j.chemosphere.2020.126169 
Lu, W. X., Rui, H. D., Liang, C. Y., Jiang, L., Zhao, S. P., & Li, K. Q. (2020). A 
Method  Based  on  GA-CNN-LSTM  for  Daily  Tourist  Flow  Prediction  at 
Scenic Spots. Entropy, 22(3), 18. doi:10.3390/e22030261 
Qingwen Jin, X. F., Jian Liu, Zhuxin Xue and Hongdeng Jian (2019). Using eXtreme 
Gradient BOOSTing to Predict Changes in Tropical Cyclone In-tensity over 
the Western North Pacific.  
Schmidhuber, H. (1997). LONG SHORT-TERM MEMORY.  
Tianqi Chen, C. G. (2016). XGBoost: A Scalable Tree Boosting System.  
Wang, L. L. Y. Y. F. H. K. W. Q. (2019). Integrating Local CNN and Global CNN 
for Script Identification in Natural Sce-ne Images. IEEE, 7, 52669-52679.  
Wang, Q. C. S. W. Q. L. W. Z. L. (2018). MV-RNN: A Multi-View Recurrent Neural 
Network for Sequential Recommen-dation. IEEE, 32, 317-331.  
Xiangzeng  Zhou,  L.  X.,  Peng  Zhang  &  Yanning  Zhang  (2017).  Online  object 
tracking  based  on  BLSTM-RNN  with  contextual-sequential  label-ing. 
Journal of Ambient Intelligence and Humanized Computing, 861-870.  
Yen-Liang Chen, M.-H. K., Shin-Yi Wu, Kwei Tang. (2009). Discovering recen-cy, 
frequency,  and  monetary  (RFM)  sequential  patterns  from  customers’  pur-
chasing data. ELSEVIER, 8(5), 241-251.  
Zhang, P., Wang & Li. (2019). Forecasting Hotel Accommodation Demand Based 
on LSTM Model Incorporating Internet Search Index.  
Zhong, J. C., Sun, Y. S., Peng, W., Xie, M. Z., Yang, J. H., & Tang, X. W. (2018). 
XGBFEMF: An XGBoost-Based Framework for Essential Protein Prediction. 
Ieee  Transactions  on  Nanobioscience,  17(3),  243-250. 
doi:10.1109/tnb.2018.2842219 <br/>

<h4>其他等我心情好之後再補<h4>


