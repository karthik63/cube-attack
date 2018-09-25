	
    
def callfunc1(maxterm,const,secretvariables,coeff):
	coeff={}
	m1=['v2','v13','v20','v24','v37','v42','v43','v46','v53','v55','v57','v67']
	m2=['v2','v12','v17','v25','v37','v39','v46','v48','v54','v56','v65','v78']
	m3=['v3','v14','v21','v25','v38','v43','v44','v47','v53','v54','v56','v58','v68']
	m4=['v3','v13','v18','v26','v38','v40','v47','v49','v55','v57','v66','v79']
	m5=['v0','v5','v7','v18','v21','v32','v38','v43','v59','v67','v73','v78']
	m6=['v1','v6','v8','v19','v22','v33','v39','v44','v60','v68','v74','v79']
	m7=['v11','v18','v20','v33','v45','v47','v53','v60','v61','v63','v69','v78']
	m8=['v5','v14','v16','v18','v27','v31','v37','v43','v48','v55','v63','v78']
	m9=['v1','v3','v6','v7','v12','v18','v22','v38','v47','v58','v67','v74']
	m10=['v1','v12','v19','v23','v36','v41','v42','v45','v52','v54','v56','v66']
	m11=['v0','v4','v9','v11','v22','v24','v27','v29','v44','v46','v51','v76']
	m12=['v0','v5','v8','v11','v13','v21','v22','v26','v36','v38','v53','v79']
	m13=['v0','v5','v8','v11','v13','v22','v26','v36','v37','v38','v53','v79']
	m14=['v2','v5','v7','v10','v14','v24','v27','v39','v49','v56','v57','v61']
	m15=['v0','v2','v9','v11','v13','v37','v44','v47','v49','v68','v74','v78']
	m16=['v1','v6','v7','v12','v18','v21','v29','v33','v34','v45','v49','v70']
	m17=['v8','v11','v15','v17','v23','v26','v32','v42','v51','v62','v64','v79']
	m18=['v0','v10','v16','v19','v28','v31','v43','v50','v53','v66','v69','v79']
	m19=['v4','v9','v10','v15','v21','v24','v32','v36','v37','v48','v52','v73']
	m20=['v7','v10','18','v20','v23','v25','v31','v45','v53','v63','v71','v78']
	m21=['v11','v16','v20','v22','v35','v43','v46','v51','v55','v58','v62','v63']
	m22=['v10','v13','v15','v17','v30','v37','v39','v42','v47','v57','v73','v79']
	m23=['v2','v4','v21','v23','v25','v41','v44','v54','v58','v66','v73','v78']
	m24=['v3','v6','v14','v21','v23','v27','v32','v40','v54','v57','v70','v71']
	m25=['v3','v5','v14','v16','v18','v20','v33','v56','v57','v65','v73','v75']
	m26=['v6','v11','v14','v19','v33','v39','v44','v52','v58','v60','v74','v79']
	m27=['v1','v7','v12','v18','v21','v25','v29','v45','v46','v61','v68','v70']
	m28=['v2','v8','v13','v19','v22','v26','v30','v46','v47','v62','v69','v71']
	m29=['v3','v9','v14','v20','v23','v27','v31','v47','v48','v63','v70','v72']
	m30=['v4','v10','v15','v21','v24','v28','v32','v48','v49','v64','v71','v73']
	m31=['v2','v4','v6','v12','v23','v29','v32','v37','v46','v49','v52','v76']
	m32=['v0','v5','v7','v12','v18','v21','v32','v38','v43','v59','v73','v78']
	m33=['v1','v6','v8','v14','v19','v22','v33','v39','v44','v60','v74','v79']
	m34=['v2','v4','v5','v8','v15','v19','v27','v32','v35','v57','v71','v78']
	m35=['v0','v3','v4','v9','v20','v28','v33','v41','v54','v58','v72','v79']
	m36=['v8','v11','v13','v17','v23','v25','v35','v45','v47','v54','v70','v79']
	m37=['v0','v6','v10','v16','v19','v31','v43','v50','v66','v69','v77','v79']
	m38=['v2','v15','v17','v20','v21','v37','v39','v44','v46','v56','v67','v73']
	m39=['v1','v16','v20','v22','v34','v37','v38','v53','v58','v69','v71','v78']
	m40=['v2','v7','v14','v22','v41','v45','v48','v58','v68','v70','v72','v76']
	m41=['v3','v14','v16','v18','v20','v23','v32','v46','v56','v57','v65','v73']
	m42=['v0','v6','v10','v16','v18','v28','v31','v43','v53','v69','v77','v79']
	m43=['v2','v8','v11','v13','v28','v31','v35','v37','v49','v51','v68','v78']
	m44=['v5','v8','v20','v32','v36','v39','v45','v51','v65','v69','v76','v78']
	m45=['v2','v4','v10','v14','v16','v22','v25','v44','v49','v51','v57','v78']
	m46=['v1','v12','v19','v23','v36','v41','v42','v45','v52','v56','v69','v75']
	m47=['v1','v7','v8','v13','v21','v23','v28','v30','v47','v68','v71','v75']
	m48=['v5','v8','v9','v12','v16','v18','v23','v40','v44','v63','v66','v70']
	m49=['v2','v11','v21','v24','v32','v55','v57','v60','v63','v66','v70','v77']
	m50=['v4','v7','v10','v18','v20','v25','v50','v53','v61','v63','v71','v78']
	m51=['v5','v12','v16','v19','v22','v36','v47','v55','v63','v71','v77','v79']
	m52=['v4','v9','v18','v21','v23','v27','v32','v38','v43','v58','v67','v79']
	m53=['v1','v7','v9','v14','v18','v21','v33','v40','v45','v49','v59','v68']
	m54=['v2','v6','v12','v13','v19','v23','v30','v48','v55','v59','v69','v79']
	m55=['v5','v7','v10','v13','v15','v17','v28','v40','v47','v73','v76','v79']
	m56=['v13','v21','v24','v39','v42','v46','v48','v51','v55','v61','v72','v78']
	m57=['v2','v4','v10','v11','v19','v34','v47','v55','v56','v58','v69','v77']
	m58=['v5','v7','v10','v15','v17','v35','v40','v47','v52','v57','v76','v79']
	m59=['v8','v11','v13','v17','v23','v25','v35','v47','v62','v64','v68','v79']
	m60=['v2','v3','v13','v15','v19','v29','v32','v37','v39','v51','v76','v79']
	m61=['v5','v7','v10','v13','v15','v17','v35','v40','v52','v70','v76','v79']
	m62=['v5','v20','v24','v29','v33','v35','v37','v39','v63','v65','v74','v78']
	m63=['v1','v12','v19','v23','v36','v41','v52','v54','v56','v66','v69','v75']
	
	
	
	if (cmp(maxterm,m1)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x0']=1
		coeff['x9']=1
		coeff['x50']=1
		const=1
		return coeff,const
	#1+x0+x9+x50 {2,13,20,24,37,42,43,46,53,55,57,67} 675
	
	if (cmp(maxterm,m2)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x0']=1
		coeff['x24']=1
		const=1
		return coeff,const
	
	#1+x0+x24 {2,12,17,25,37,39,46,48,54,56,65,78} 673
	if (cmp(maxterm,m3)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x1']=1
		coeff['x10']=1
		coeff['x51']=1
		const=1
		return coeff,const
	#1+x1+x10+x51 {3,14,21,25,38,43,44,47,54,56,58,68} 674
	
	if (cmp(maxterm,m4)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x1']=1
		coeff['x25']=1
		#coeff['x51']=1
		
		const=1
		return coeff,const

	#1+x1+x25 {3,13,18,26,38,40,47,49,55,57,66,79} 672
	if (cmp(maxterm,m5)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x2']=1
		coeff['x34']=1
		coeff['x62']=1
		
		const=1
		return coeff,const
	#1+x2+x34+x62 {0,5,7,18,21,32,38,43,59,67,73,78} 678
	if (cmp(maxterm,m6)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x3']=1
		coeff['x35']=1
		coeff['x63']=1
		
		const=1
		return coeff,const
	#1+x3+x35+x63 {1,6,8,19,22,33,39,44,60,68,74,79} 677
	if (cmp(maxterm,m7)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x4']=1
		#coeff['x10']=1
		#coeff['x51']=1
		
		const=0
		return coeff,const
	#x4 {11,18,20,33,45,47,53,60,61,63,69,78} 675
	if (cmp(maxterm,m8)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x5']=1
		
		const=0
		return coeff,const
	#x5 {5,14,16,18,27,31,37,43,48,55,63,78} 677
	if (cmp(maxterm,m9)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x7']=1
		
		const=0
		return coeff,const

	#x7 {1,3,6,7,12,18,22,38,47,58,67,74} 675
	if (cmp(maxterm,m10)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x8']=1
		coeff['x49']=1
		coeff['x68']=1
		
		const=1
		return coeff,const
	#1+x8+x49+x68 {1,12,19,23,36,41,42,45,52,54,56,66} 676
	if (cmp(maxterm,m11)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x11']=1
		
		const=0
		return coeff,const
	#x11 {0,4,9,11,22,24,27,29,44,46,51,76} 684
	if (cmp(maxterm,m12)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x12']=1
		const=0
		return coeff,const
	#x12 {0,5,8,11,13,21,22,26,36,38,53,79} 673
	if (cmp(maxterm,m13)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x13']=1
		const=0
		return coeff,const
	#x13 {0,5,8,11,13,22,26,36,37,38,53,79} 673
	if (cmp(maxterm,m14)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x14']=1
		const=1
		return coeff,const
	#1+x14 {2,5,7,10,14,24,27,39,49,56,57,61} 672
	if (cmp(maxterm,m15)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x15']=1
		const=0
		return coeff,const
	#x15 {0,2,9,11,13,37,44,47,49,68,74,78} 685
	if (cmp(maxterm,m16)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x16']=1
		const=0
		return coeff,const
	#x16 {1,6,7,12,18,21,29,33,34,45,49,70} 675
	if (cmp(maxterm,m17)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x17']=1
		const=0
		return coeff,const
	#x17 {8,11,15,17,26,23,32,42,51,62,64,79} 677
	if (cmp(maxterm,m18)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x18']=1
		const=0
		return coeff,const
	#x18 {0,10,16,19,28,31,43,50,53,66,69,79} 676
	if (cmp(maxterm,m19)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x19']=1
		const=0
		return coeff,const
	#x19 {4,9,10,15,21,24,32,36,37,48,52,73} 672
	if (cmp(maxterm,m20)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x20']=1
		const=0
		return coeff,const
	#x20 {7,10,18,20,23,25,31,45,53,63,71,78} 675
	if (cmp(maxterm,m21)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x20']=1
		coeff['x50']=1
		const=1
		return coeff,const
	#1+x20+x50 {11,16,20,22,35,43,46,51,55,58,62,63} 675
	if (cmp(maxterm,m22)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x21']=1
		coeff['x66']=1
		const=1
		return coeff,const
	#1+x21+x66 {10,13,15,17,30,37,39,42,47,57,73,79} 673
	if (cmp(maxterm,m23)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x22']=1
		const=0
		return coeff,const
	#x22 {2,4,21,23,25,41,44,54,58,66,73,78} 673
	
	if (cmp(maxterm,m24)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x23']=1
		const=0
		return coeff,const
	#x23 {3,6,14,21,23,27,32,40,54,57,70,71} 672
	
	if (cmp(maxterm,m25)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x24']=1
		const=1
		return coeff,const
	#1+x24 {3,5,14,16,18,20,33,56,57,65,73,75} 672
	
	if (cmp(maxterm,m26)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x28']=1
		const=1
		return coeff,const
	#1+x28 {6,11,14,19,33,39,44,52,58,60,74,79} 676
	
	if (cmp(maxterm,m27)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x29']=1
		const=0
		return coeff,const
	#x29 {1,7,12,18,21,25,29,45,46,61,68,70} 675
	
	if (cmp(maxterm,m28)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x30']=1
		const=0
		return coeff,const
	#x30 {2,8,13,19,22,26,30,46,47,62,69,71} 674
	
	if (cmp(maxterm,m29)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x31']=1
		const=0
		return coeff,const
	#x31 {3,9,14,20,23,27,31,47,48,63,70,72} 673
	
	if (cmp(maxterm,m30)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x32']=1
		const=0
		return coeff,const
	#x32 {4,10,15,21,24,28,32,48,49,64,71,73} 672
	
	if (cmp(maxterm,m31)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x33']=1
		const=0
		return coeff,const
	#x33 {2,4,6,12,23,29,32,37,46,49,52,76} 680
	
	if (cmp(maxterm,m32)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x34']=1
		coeff['x62']=1
		const=1
		return coeff,const
	#1+x34+x62 {0,5,7,13,18,21,32,38,43,59,73,78} 678
	
	if (cmp(maxterm,m33)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x35']=1
		coeff['x32']=1
		const=1
		return coeff,const
	#1+x35+x63 {1,6,8,14,19,22,33,39,44,60,74,79} 677
	
	if (cmp(maxterm,m34)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x36']=1
		const=0
		return coeff,const
	#x36 {2,4,5,8,15,19,27,32,35,57,71,78} 677
	
	if (cmp(maxterm,m35)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x38']=1
		coeff['x56']=1
		const=0
		return coeff,const
	#x38+x56 {0,3,4,9,20,28,33,41,54,58,72,79} 678
	
	if (cmp(maxterm,m36)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x39']=1
		coeff['x57']=1
		coeff['x66']=1
		const=1
		return coeff,const
	#1+x39+x57+x66 {8,11,13,17,23,25,35,45,47,54,70,79} 674
	
	if (cmp(maxterm,m37)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x40']=1
		coeff['x58']=1
		coeff['x64']=1
		const=0
		return coeff,const
	#x40+x58+x64 {0,6,10,16,19,31,43,50,66,69,77,79} 676
	
	if (cmp(maxterm,m38)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x41']=1
		const=1
		return coeff,const

	#1+x41 {2,15,17,20,21,37,39,44,46,56,67,73} 674
	
	if (cmp(maxterm,m39)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x42']=1
		coeff['x60']=1
		const=0
		return coeff,const
	#x42+x60 {1,16,20,22,34,37,38,53,58,69,71,78} 674
	
	if (cmp(maxterm,m40)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x43']=1
		const=0
		return coeff,const
	#x43 {2,7,14,22,41,45,48,58,68,70,72,76} 673
	
	if (cmp(maxterm,m41)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x44']=1
		coeff['x62']=1
		const=0
		return coeff,const
	#x44+x62 {3,14,16,18,20,23,32,46,56,57,65,73} 672
	
	if (cmp(maxterm,m42)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x45']=1
		coeff['x64']=1
		const=1
		return coeff,const
	#1+x45+x64 {0,6,10,16,18,28,31,43,53,69,77,79} 676
	
	if (cmp(maxterm,m43)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x46']=1
		coeff['x55']=1
		const=0
		return coeff,const
	#x46+x55 {2,8,11,13,28,31,35,37,49,51,68,78} 684
	
	if (cmp(maxterm,m44)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x47']=1
		const=0
		return coeff,const
	#x47 {5,8,20,32,36,39,45,51,65,69,76,78} 676
	
	if (cmp(maxterm,m45)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x48']=1
		const=0
		return coeff,const
	#x48 {2,4,10,14,16,22,25,44,49,51,57,78} 678
	
	if (cmp(maxterm,m46)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x49']=1
		coeff['x62']=1
		const=0
		return coeff,const
	#x49+x62 {1,12,19,23,36,41,42,45,52,56,69,75} 676
	
	if (cmp(maxterm,m47)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x51']=1
		coeff['x62']=1
		const=0
		return coeff,const
	#x51+x62 {1,7,8,13,21,23,28,30,47,68,71,75} 674
	
	if (cmp(maxterm,m48)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x52']=1
		const=0
		return coeff,const
	#x52 {5,8,9,12,16,18,23,40,44,63,66,70} 674
	
	if (cmp(maxterm,m49)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x53']=1
		const=0
		return coeff,const
	#x53 {2,11,21,24,32,55,57,60,63,66,70,77} 675
	
	if (cmp(maxterm,m50)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x54']=1
		coeff['x60']=1
		const=1
		return coeff,const
	#1+x54+x60 {4,7,10,18,20,25,50,53,61,63,71,78} 675
	
	if (cmp(maxterm,m51)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x55']=1
		coeff['x64']=1
		const=0
		return coeff,const
	#x55+x64 {5,12,16,19,22,36,47,55,63,71,77,79} 674
	
	if (cmp(maxterm,m52)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x56']=1
		const=1
		return coeff,const
	#1+x56 {4,9,18,21,23,27,32,38,43,58,67,69} 677
	
	if (cmp(maxterm,m53)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x57']=1
		const=0
		return coeff,const
	#x57 {1,7,9,14,18,21,33,40,45,49,59,68} 675
	
	if (cmp(maxterm,m54)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x58']=1
		const=1
		return coeff,const
	#1+x58 {2,6,12,13,19,23,30,48,55,59,69,79} 673
	
	if (cmp(maxterm,m55)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x60']=1
		const=0
		return coeff,const
	#x60 {5,7,10,13,15,17,28,40,47,73,76,79} 681
	
	if (cmp(maxterm,m56)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x61']=1
		const=0
		return coeff,const
	#x61 {13,21,24,39,42,46,48,51,55,61,72,78} 673
	
	if (cmp(maxterm,m57)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x62']=1
		const=1
		return coeff,const
	#1+x62 {2,4,10,11,19,34,47,55,56,58,69,77} 674
	
	if (cmp(maxterm,m58)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x63']=1
		const=0
		return coeff,const
	#x63 {5,7,10,15,17,35,40,47,52,57,76,79} 674
	
	if (cmp(maxterm,m59)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x64']=1
		const=0
		return coeff,const
	#x64 {8,11,13,17,23,25,35,47,62,64,68,79} 673
	
	if (cmp(maxterm,m60)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x65']=1
		const=0
		return coeff,const
	#x65 {2,3,13,15,19,29,32,37,39,51,76,79} 682
	
	if (cmp(maxterm,m61)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x66']=1
		const=1
		return coeff,const
	#1+x66 {5,7,10,13,15,17,35,40,52,70,76,79} 678
	
	if (cmp(maxterm,m62)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x67']=1
		const=1
		return coeff,const
	#1+x67 {5,20,24,29,33,35,37,39,63,65,74,78} 677
	if (cmp(maxterm,m63)==0):
		for var in secretvariables:
			coeff[var]=0
		coeff['x68']=1
		const=1
		return coeff,const
	else:
		for var in secretvariables:
			coeff[var]=0
		const=0
		return coeff,const
	#can put an error message in this case
	#1+x68 {1,12,19,23,36,41,52,54,56,66,69,75} 676

    