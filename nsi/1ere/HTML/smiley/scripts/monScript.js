// Saisir vos fonction javaScript ici
function Q1(){
	document.getElementById('t1').innerHTML="Histoire du Smiley";
}
function Q2(){
	document.getElementById('smile').innerHTML="<img onmouseover='Clin()' src='images/smiley.svg'>";
}
function Clin(){
	document.getElementById('smile').innerHTML="<img onmouseout='Q2()' src='images/smiley2.svg'>";
}
function Q3(){
	NS=document.getElementById('NS').value;
	NM=document.getElementById('NM').value;
	NbrSmi=document.getElementById('smi');
	NM=Number(NM)+1
	NbrSmi.innerHTML="";
	for (i=1;i<NM;i=i+1){
		if(i==1){NbrSmi.innerHTML="Mois "+Math.round(i)+" : "+Math.round(NS)+" smiley"+"</br>"
		i=i+1};
	
		NS=NS*1.20;
		NbrSmi.innerHTML=NbrSmi.innerHTML+"Mois "+Math.round(i)+" : "+Math.round(NS)+" smileys"+"<br>";
		
	
	}
}
function Q4(){
	Smi=document.getElementById('SMILE').value;
	Smi=Number(Smi)+1;
	LesSmi=""
	for (i=1;i<Smi;i=i+1){LesSmi=LesSmi+"😊"};
		{alert(LesSmi);}
}

	