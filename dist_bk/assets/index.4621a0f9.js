import{_ as N,o as C,a as w,c as x,P as j,r as W,w as Q,b as p,d as f,u as c,T as H,p as V,e as L,f as h,i as O,s as T,g as J,t as X,h as Y,j as Z,k as ee,D as z,l as te}from"./vendor.1cd03f70.js";const ae=function(){const d=document.createElement("link").relList;if(d&&d.supports&&d.supports("modulepreload"))return;for(const a of document.querySelectorAll('link[rel="modulepreload"]'))m(a);new MutationObserver(a=>{for(const e of a)if(e.type==="childList")for(const r of e.addedNodes)r.tagName==="LINK"&&r.rel==="modulepreload"&&m(r)}).observe(document,{childList:!0,subtree:!0});function i(a){const e={};return a.integrity&&(e.integrity=a.integrity),a.referrerpolicy&&(e.referrerPolicy=a.referrerpolicy),a.crossorigin==="use-credentials"?e.credentials="include":a.crossorigin==="anonymous"?e.credentials="omit":e.credentials="same-origin",e}function m(a){if(a.ep)return;a.ep=!0;const e=i(a);fetch(a.href,e)}};ae();const oe={id:"map",style:{width:"100vw"}},le={setup(u){function d(i={lon:121,lat:23.7}){var m=[{type:"scattermapbox",text:[],lon:[],lat:[]}],a={dragmode:"zoom",mapbox:{center:{lon:i.lon,lat:i.lat},zoom:6.8,style:"white-bg",layers:[{sourcetype:"raster",source:["https://wmts.nlsc.gov.tw/wmts/EMAP/default/EPSG:3857/{z}/{y}/{x}"],below:"traces"},{below:"traces",sourcetype:"geojson",source:"/taiwan_county_geojson_mini.json",type:"line",color:"purple",opacity:.4,line:{width:1}}]},margin:{r:0,t:0,b:0,l:0},showlegend:!1},e={doubleClick:!0,doubleClickDelay:10,responsive:!0,autosize:!0,displayModeBar:!1};j.newPlot("map",m,a,e)}return C(()=>{d()}),(i,m)=>(w(),x("div",oe))}};var se=N(le,[["__scopeId","data-v-07a0511c"]]);const A=u=>(V("data-v-7bc35ce4"),u=u(),L(),u),re={id:"navbar",class:"overlay",style:{"z-index":"100","background-color":"rgba(240, 245, 240, 0.95)","box-shadow":"0 -1px 24px rgba(0, 0, 0, 0.4)"}},ne=A(()=>p("ul",{class:"nav nav-tabs pt-5 mt-3",id:"myTab",role:"tablist"},[p("li",{class:"nav-item w-50",role:"presentation"},[p("button",{class:"nav-link active w-100",id:"home-tab","data-bs-toggle":"tab","data-bs-target":"#home",type:"button",role:"tab","aria-controls":"home","aria-selected":"true"}," \u5EE0\u5546\u5217\u8868 ")]),p("li",{class:"nav-item w-50",role:"presentation"},[p("button",{class:"nav-link w-100",id:"profile-tab","data-bs-toggle":"tab","data-bs-target":"#profile",type:"button",role:"tab","aria-controls":"profile","aria-selected":"false"}," \u7D71\u8A08\u5716 ")])],-1)),ie={class:"tab-content",id:"myTabContent"},ce={class:"tab-pane fade show active",id:"home",role:"tabpanel","aria-labelledby":"home-tab",style:{height:"calc(100vh - 200px)",overflow:"scroll"}},de=A(()=>p("div",{class:"tab-pane fade",id:"profile",role:"tabpanel","aria-labelledby":"profile-tab"}," ... ",-1)),pe={props:{data:Object,time:Array,chem:String,operation:String},setup(u){const d=u;C(()=>{a()});var i=W({isloading:!1,columns:[{label:"\u5EE0\u5546\u540D\u7A31",field:"ComFacBizName_m",width:"60%",sortable:!0,display:e=>`${e.ComFacBizName_m}`},{label:"\u904B\u4F5C\u91CF",field:"Quantity",width:"40%",sortable:!0,display:e=>`${e.Quantity} \u516C\u5678`}],rows:[],sortable:{order:"id",sort:"asc"}});Q(()=>[d.data],(e,r)=>{i.rows=e[0];let o=document.querySelector(".vtl-paging");console.log(o),console.log(e[0])});function m(){let e=document.querySelector(".vtl-paging");[...e.children].forEach(r=>{r.className=r.className.replace("col-sm-12","col-12").replace("col-md-4","")}),console.log(e)}function a(){document.querySelector(".togglebtn").addEventListener("click",e=>{let r=document.getElementById("navbar").style.width;document.body.clientWidth>768?r==="340px"|!r?document.getElementById("navbar").style.width="0%":document.getElementById("navbar").style.width="340px":r==="0%"|!r?document.getElementById("navbar").style.width="100%":document.getElementById("navbar").style.width="0%"})}return(e,r)=>(w(),x("div",re,[ne,p("div",ie,[p("div",ce,[f(c(H),{"is-static-mode":!0,"is-loading":c(i).isLoading,columns:c(i).columns,rows:c(i).rows,total:c(i).totalRecordCount,sortable:c(i).sortable,onIsFinished:m},null,8,["is-loading","columns","rows","total","sortable"])]),de])]))}};var ue=N(pe,[["__scopeId","data-v-7bc35ce4"]]);const F=[{index:0,label:"2021 \u7B2C\u4E00\u5B63"},{index:1,label:"2021 \u7B2C\u4E8C\u5B63"},{index:2,label:"2021 \u7B2C\u4E09\u5B63"},{index:3,label:"2021 \u7B2C\u56DB\u5B63"},{index:4,label:"\u6700\u65B0\u7533\u5831"}];const P=u=>(V("data-v-297186b2"),u=u(),L(),u),me={id:"searchbar",class:"fixed-top"},ge={class:"container-xs px-0"},_e={class:"row rounded-lg mx-0"},ve=P(()=>p("div",{class:"col-2 togglebtn noselect"},"\u2630",-1)),he={class:"col-3 border-end ps-2"},fe={class:"col-7 ps-2"},ye={slot:"tag","slot-scope":"{ option, remove }"},be={class:"custom__tag"},we={slot:"clear","slot-scope":"props"},xe=P(()=>p("span",{slot:"noResult"},"Oops! No elements found. Consider changing the search query.",-1)),$e={props:{selectedtime:Array},emits:["item"],setup(u,{emit:d}){const i=u;var m=h("");const a=[{chn:"\u8F38\u5165",eng:"import"},{chn:"\u8CAF\u5B58",eng:"storage"},{chn:"\u88FD\u9020",eng:"produce"},{chn:"\u4F7F\u7528",eng:"usage"}];var e=h(""),r=h(""),o=h([]),s=h(!1);const _=async g=>{s.value=!0;let l="/explosiveapi";console.log(1),console.log(`${l}/chemilist`);let n=await fetch(`${l}/chemilist`).then(v=>v.json());console.log(2),o.value=n.map(v=>v.label),s.value=!1};function b(g,l){return g.reduce(function(n,v){return n[v[l]]?n[v[l]].push(v):n[v[l]]=[v],n},{})}return Q([e,r,()=>i.selectedtime],async([g,l,n],[v,E,I])=>{if(g!=""&l!=""&(v!=g|E!=l|I!=n)){let D=l.split(" ")[1],q=a.filter(y=>y.chn===g)[0].eng;var t=[];let B=`/explosiveapi/records_all/?name=${D}&operation=${q}`;if(n[0]==="\u6700\u65B0\u7533\u5831"){let y=await fetch(B).then(k=>k.json());var M=b(y,"ComFacBizName");m.value=Object.keys(M).length,Object.values(M).forEach(k=>{var R=b(k,"deptid");Object.values(R).forEach(U=>{t.push(U.sort(function(G,K){return parseFloat(K.time)-parseFloat(G.time)})[0])})})}else{var S,$=[];n.forEach(y=>{$.push(y.replace(" \u7B2C\u4E00\u5B63","01").replace(" \u7B2C\u4E8C\u5B63","04").replace(" \u7B2C\u4E09\u5B63","07").replace(" \u7B2C\u56DB\u5B63","10"))}),$[1]==="\u6700\u65B0\u7533\u5831"?S=`Time_gte=${$[0]}`:S=`Time_gte=${$[0]}&Time_lte=${$[1]}`,B=`${B}&${S}`,t=await fetch(B).then(y=>y.json())}d("item",{res:t,selected:{operation:g,chem:l}})}}),C(()=>{}),(g,l)=>(w(),x("div",me,[p("div",ge,[p("div",_e,[ve,p("div",he,[f(c(T),{modelValue:c(e),"onUpdate:modelValue":l[0]||(l[0]=n=>O(e)?e.value=n:e=n),placeholder:"\u884C\u70BA",options:a.map(n=>n.chn),searchable:!1,"close-on-select":!0,"show-labels":!1},null,8,["modelValue","options"])]),p("div",fe,[f(c(T),{modelValue:c(r),"onUpdate:modelValue":l[3]||(l[3]=n=>O(r)?r.value=n:r=n),placeholder:"\u5316\u5B78\u7269\u8CEA","open-direction":"bottom",options:c(o),searchable:!0,loading:c(s),"close-on-select":!0,"show-labels":!1,onSearchChange:_},{default:J(()=>[p("template",ye,[p("span",be,[p("span",null,X(g.option.name),1),p("span",{class:"custom__remove",onClick:l[1]||(l[1]=n=>g.remove(g.option))},"\u274C")])]),p("template",we,[c(r).length?(w(),x("div",{key:0,class:"multiselect__clear",onMousedown:l[2]||(l[2]=Y(n=>g.clearAll(i.search),["prevent","stop"]))},null,32)):Z("",!0)]),xe]),_:1},8,["modelValue","options","loading"])])])])]))}};var Ie=N($e,[["__scopeId","data-v-297186b2"]]);const Be={class:"fixed-bottom",id:"timeslider"},Ne={props:{selectedtime:Array},emits:["time"],setup(u,{emit:d}){const i=u;function m(){let o=F.filter(s=>i.selectedtime.includes(s.label)).map(s=>s.index);return o.length==1?[...o,...o]:o}const a=h(m());function e(o){return F.filter(s=>s.index===o)[0].label}function r(o){console.log(o),d("time",F.filter(s=>o.includes(s.index)))}return C(()=>{}),(o,s)=>(w(),x("div",Be,[f(c(ee),{modelValue:a.value,"onUpdate:modelValue":s[0]||(s[0]=_=>a.value=_),min:0,max:4,format:e,onChange:r},null,8,["modelValue"])]))}};var Ce=N(Ne,[["__scopeId","data-v-09376425"]]);const Ee={props:{data:Object,time:Array,chem:String,operation:String},setup(u){const d=u;return h([]),Q(()=>[d.data,d.time,d.chem,d.operation],(i,m)=>{let[a,e,r,o]=i;var s=new z(a).groupBy("time","operation","name","city").aggregate(t=>t.stat.sum("Quantity")).rename("aggregation","Quantity");new z(a);var _=new z(a).cast("lon",t=>String(t)).cast("lat",t=>String(t)).groupBy("time","operation","name","lon","lat","ComFacBizName_m").aggregate(t=>t.stat.sum("Quantity")).rename("aggregation","Quantity");e[0]==="\u6700\u65B0\u7533\u5831"?(s=s.sortBy(["time","operation","name","city"],!0),s=s.dropDuplicates("operation","name","city"),_=_.sortBy(["time","operation","name"],!0),_=_.dropDuplicates("operation","name","lon","lat")):o==="\u8CAF\u5B58"?(s=s.sortBy(["Quantity","time","operation","name","city"],!0).dropDuplicates("operation","name","city"),_=_.sortBy(["Quantity","time","operation","name","lon","lat"],!0).dropDuplicates("operation","name","lon","lat")):(s=s.groupBy("operation","name","city").aggregate(t=>t.stat.sum("Quantity")).rename("aggregation","Quantity"),_=_.groupBy("operation","name","lon","lat").aggregate(t=>t.stat.sum("Quantity")).rename("aggregation","Quantity"));var b=s.toCollection(),g=_.toCollection(),l="%{location}<br>TIMEINFO%{z:.2f}\u516C\u5678";o==="\u8CAF\u5B58"?e[0]==="\u6700\u65B0\u7533\u5831"?l=l.replace("TIMEINFO","\u6700\u65B0\u671F\u5225\uFF1A%{text}<br>"):l=l.replace("TIMEINFO","\u6700\u5927\u671F\u5225\uFF1A%{text}<br>"):l=l.replace("TIMEINFO","");let n=g.map(t=>t.Quantity);n=n.map(t=>t/Math.max(...n)+16);var v=[{name:"",type:"choroplethmapbox",geojson:"/taiwan_county_geojson_mini.json",locations:b.map(t=>t.city),text:o==="\u8CAF\u5B58"?b.map(t=>t.time):" ",hovertemplate:l,hoverlabel:{font:{size:22}},featureidkey:"properties.NAME_2014",z:b.map(t=>t.Quantity),showscale:!1,zmin:0,colorscale:[[0,"rgba(255,200,200,.5)"],[1,"rgba(222,30,20,.7)"]]},{lon:g.map(t=>t.lon),lat:g.map(t=>t.lat),text:g.map(t=>`${t.ComFacBizName_m}:<br> ${t.Quantity}`),type:"scattermapbox",name:"",hovertemplate:"%{text} \u516C\u5678",marker:{color:"rgba(58,99,73,.95)",size:n}}];let E=document.querySelector("#map").data.length,I=[];for(let t=1;t<E;t++)I.push(-t);j.deleteTraces("map",I),j.addTraces("map",v)}),(i,m)=>null}};const Se={setup(u){var d=h(["\u6700\u65B0\u7533\u5831","\u6700\u65B0\u7533\u5831"]),i=h(""),m=h(""),a=h([]);function e(o){i.value=o.selected.chem,m.value=o.selected.operation,a.value=o.res}function r(o){o.length==1&&(o=[...o,...o]),d.value=o.map(s=>s.label)}return(o,s)=>(w(),x("div",null,[f(se),f(Ie,{onItem:e,selectedtime:c(d)},null,8,["selectedtime"]),f(ue,{data:c(a),time:c(d),chem:c(i),operation:c(m)},null,8,["data","time","chem","operation"]),f(Ce,{onTime:r,selectedtime:c(d)},null,8,["selectedtime"]),f(Ee,{data:c(a),time:c(d),chem:c(i),operation:c(m)},null,8,["data","time","chem","operation"])]))}};let ke=te(Se);ke.mount("#app");
