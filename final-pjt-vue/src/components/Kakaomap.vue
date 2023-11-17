<template>
    <div class="map_wrap">
      <div>
        <div class="search_option">
            <span>
              <label for="sido1">시/도</label>
              <select v-model="selectLocal1">
                <option v-for="local1 in localType1" :value="local1">{{ local1 }}</option>            
              </select>
            </span>
            <span>
              <label for="gugun1">구/군</label>
              <select v-model="selectLocal2">
                <option v-for="local2 in localType2" :value="local2">{{ local2 }}</option>            
              </select>
            </span>
            <span>
              <label for="dong1">동</label>
              <select v-model="selectLocal3">
                <option v-for="local3 in localType3" :value="local3">{{ local3 }}</option>            
              </select>
            </span>
            <span>
              <label for="bank1">검색은행</label>
              <select v-model="selectedBank">
                <option v-for="bank in banks" :key="bank">{{ bank }}</option>
              </select>
            </span>
          </div>
          <button @click="searchPlaces">검색하기</button>
      </div>
      <div id="map" style="width:90%;height:500px;position:relative;overflow:hidden;"></div>
      <div id="menu_wrap" class="bg_white">
        <ul id="placesList"></ul>
        <div id="pagination"></div> 
      </div>
  </div>
  </template>


<style scoped>
.map_wrap, .map_wrap * {margin:0;padding:0;font-family:'Malgun Gothic',dotum,'돋움',sans-serif;font-size:12px;}
.map_wrap a, .map_wrap a:hover, .map_wrap a:active{color:#000;text-decoration: none;}
.map_wrap {position:relative;width:100%;height:500px;}
#menu_wrap {position:absolute;top:20%;left:0;bottom:0;width:250px;margin:10px 0 30px 10px;padding:5px;overflow-y:auto;background:rgba(255, 255, 255, 0.7);z-index: 1;font-size:12px;border-radius: 10px;}
.bg_white {background:#fff;}
#menu_wrap hr {display: block; height: 1px;border: 0; border-top: 2px solid #5F5F5F;margin:3px 0;}
#menu_wrap .option{text-align: center;}
#menu_wrap .option p {margin:10px 0;}  
#menu_wrap .option button {margin-left:5px;}
#placesList li {list-style: none;}
#placesList .item {position:relative;border-bottom:1px solid #888;overflow: hidden;cursor: pointer;min-height: 65px;}
#placesList .item span {display: block;margin-top:4px;}
#placesList .item h5, #placesList .item .info {text-overflow: ellipsis;overflow: hidden;white-space: nowrap;}
#placesList .item .info{padding:10px 0 10px 55px;}
#placesList .info .gray {color:#8a8a8a;}
#placesList .info .jibun {padding-left:26px;background:url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/places_jibun.png) no-repeat;}
#placesList .info .tel {color:#009900;}
#placesList .item .markerbg {float:left;position:absolute;width:36px; height:37px;margin:10px 0 0 10px;background:url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png) no-repeat;}
#placesList .item .marker_1 {background-position: 0 -10px;}
#placesList .item .marker_2 {background-position: 0 -56px;}
#placesList .item .marker_3 {background-position: 0 -102px}
#placesList .item .marker_4 {background-position: 0 -148px;}
#placesList .item .marker_5 {background-position: 0 -194px;}
#placesList .item .marker_6 {background-position: 0 -240px;}
#placesList .item .marker_7 {background-position: 0 -286px;}
#placesList .item .marker_8 {background-position: 0 -332px;}
#placesList .item .marker_9 {background-position: 0 -378px;}
#placesList .item .marker_10 {background-position: 0 -423px;}
#placesList .item .marker_11 {background-position: 0 -470px;}
#placesList .item .marker_12 {background-position: 0 -516px;}
#placesList .item .marker_13 {background-position: 0 -562px;}
#placesList .item .marker_14 {background-position: 0 -608px;}
#placesList .item .marker_15 {background-position: 0 -654px;}
#pagination {margin:10px auto;text-align: center;}
#pagination a {display:inline-block;margin-right:10px;}
#pagination .on {font-weight: bold; cursor: default;color:#777;}

.search_option {
  display: flex;
  margin-bottom: 50px;
}

.search_option span {
  margin-right: 10px;
}
</style>
  
<script setup>
import { ref, onMounted, computed, watch } from 'vue';
    
import { useCounterStore } from '@/stores/counter'

import local from "@/assets/region.json"
  
  const map = ref(null);
  const infowindow = ref(null); // infowindow 추가
  const markers = ref([])
  let marker = ''
  const keyword = ref('')
  
  const MAP_API_KEY = import.meta.env.VITE_MAP_API_KEY

  
  onMounted(() => {
    if (window.kakao && window.kakao.maps) {
      loadMap();
    } else {
      loadScript();
    }
  });
  


  
  // api 스크립트 불러오기
  const loadScript = () => {
    const script = document.createElement("script");
    script.src =
      `//dapi.kakao.com/v2/maps/sdk.js?appkey=${MAP_API_KEY}&libraries=services&autoload=false`;
    script.onload = () => window.kakao.maps.load(loadMap);
    document.head.appendChild(script);
  };
  
  // 맵 출력하기
  const loadMap = () => {
    const container = document.getElementById("map");
    const options = {
      center: new window.kakao.maps.LatLng(37.566826, 126.9786567),
      level: 4,
    };
  
    map.value = new window.kakao.maps.Map(container, options);
    infowindow.value = new window.kakao.maps.InfoWindow({ zIndex: 1 }); // Correct initialization
    
    // 키워드로 장소를 검색합니다
    
    // 키워드 검색을 요청하는 함수입니다

    // 지도 확대 축소를 제어할 수 있는  줌 컨트롤을 생성합니다
    var zoomControl = new kakao.maps.ZoomControl();
    map.value.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);
  
  };
  const searchPlaces = function() {
      // preventDefault()
      const keywordValue = `${selectLocal1.value} ${selectLocal2.value} ${selectLocal3.value} ${selectedBank.value}` 
      if (!keywordValue) {
        alert('키워드를 입력해주세요!');
        return;
      }
      const ps = new kakao.maps.services.Places();
      // 장소검색 객체를 통해 키워드로 장소검색을 요청합니다
      ps.keywordSearch(keywordValue, placesSearchCB); 
    }
  function placesSearchCB(data, status, pagination) {
      if (status === kakao.maps.services.Status.OK) {
  
          // 정상적으로 검색이 완료됐으면
          // 검색 목록과 마커를 표출합니다
          displayPlaces(data);
  
          // 페이지 번호를 표출합니다
          displayPagination(pagination);
  
      } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
  
          alert('검색 결과가 존재하지 않습니다.');
          return;
  
      } else if (status === kakao.maps.services.Status.ERROR) {
  
          alert('검색 결과 중 오류가 발생했습니다.');
          return;
  
      }
  }
  
  // 검색 결과 목록과 마커를 표출하는 함수입니다
  function displayPlaces(places) {
  
      var listEl = document.getElementById('placesList'), 
      menuEl = document.getElementById('menu_wrap'),
      fragment = document.createDocumentFragment(), 
      bounds = new kakao.maps.LatLngBounds(), 
      listStr = '';
      
      // 검색 결과 목록에 추가된 항목들을 제거합니다
      removeAllChildNods(listEl);
  
      // 지도에 표시되고 있는 마커를 제거합니다
      removeMarker();
      
      for ( var i=0; i<places.length; i++ ) {
  
          // 마커를 생성하고 지도에 표시합니다
          var placePosition = new kakao.maps.LatLng(places[i].y, places[i].x),
          marker = addMarker(placePosition, i, places[i].place_name), 
              itemEl = getListItem(i, places[i]); // 검색 결과 항목 Element를 생성합니다
  
          // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
          // LatLngBounds 객체에 좌표를 추가합니다
          bounds.extend(placePosition);
          // 마커와 검색결과 항목에 mouseover 했을때
          // 해당 장소에 인포윈도우에 장소명을 표시합니다
          // mouseout 했을 때는 인포윈도우를 닫습니다
          (function(marker, title) {
              kakao.maps.event.addListener(marker, 'mouseover', function() {
                  displayInfowindow(marker, title);
              });
  
              kakao.maps.event.addListener(marker, 'mouseout', function() {
                  infowindow.value.close();
              });
  
              itemEl.onmouseover =  function () {
                  displayInfowindow(marker, title);
              };
  
              itemEl.onmouseout =  function () {
                  infowindow.value.close();
              };
          })(marker, places[i].place_name);
  
          fragment.appendChild(itemEl);
      }
  
      // 검색결과 항목들을 검색결과 목록 Element에 추가합니다
      listEl.appendChild(fragment);
      menuEl.scrollTop = 0;
      // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
      
      map.value.setBounds(bounds);
      
  }
  
  // 검색결과 항목을 Element로 반환하는 함수입니다
  function getListItem(index, places) {
  
      var el = document.createElement('li'),
      itemStr = '<span class="markerbg marker_' + (index+1) + '"></span>' +
                  '<div class="info">' +
                  '   <h5>' + places.place_name + '</h5>';
  
      if (places.road_address_name) {
          itemStr += '    <span>' + places.road_address_name + '</span>' +
                      '   <span class="jibun gray">' +  places.address_name  + '</span>';
      } else {
          itemStr += '    <span>' +  places.address_name  + '</span>'; 
      }
                  
        itemStr += '  <span class="tel">' + places.phone  + '</span>' +
                  '</div>';           
  
      el.innerHTML = itemStr;
      el.className = 'item';
  
      return el;
  }
  
  // 마커를 생성하고 지도 위에 마커를 표시하는 함수입니다
  function addMarker(position, idx, title) {
      var imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png', // 마커 이미지 url, 스프라이트 이미지를 씁니다
          imageSize = new kakao.maps.Size(36, 37),  // 마커 이미지의 크기
          imgOptions =  {
              spriteSize : new kakao.maps.Size(36, 691), // 스프라이트 이미지의 크기
              spriteOrigin : new kakao.maps.Point(0, (idx*46)+10), // 스프라이트 이미지 중 사용할 영역의 좌상단 좌표
              offset: new kakao.maps.Point(13, 37) // 마커 좌표에 일치시킬 이미지 내에서의 좌표
          },
          markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions),
              marker = new kakao.maps.Marker({
              position: position, // 마커의 위치
              image: markerImage 
          }); 
  
      marker.setMap(map.value); // 지도 위에 마커를 표출합니다
      markers.value.push(marker);  // 배열에 생성된 마커를 추가합니다
  
      return marker;
  }
  
  // 지도 위에 표시되고 있는 마커를 모두 제거합니다
  function removeMarker() {
      for ( var i = 0; i < markers.value.length; i++ ) {
          markers.value[i].setMap(null);
      }   
      markers.value = [];
  }
  
  // 검색결과 목록 하단에 페이지번호를 표시는 함수입니다
  function displayPagination(pagination) {
      var paginationEl = document.getElementById('pagination'),
          fragment = document.createDocumentFragment(),
          i; 
  
      // 기존에 추가된 페이지번호를 삭제합니다
      while (paginationEl.hasChildNodes()) {
          paginationEl.removeChild (paginationEl.lastChild);
      }
  
      for (i=1; i<=pagination.last; i++) {
          var el = document.createElement('a');
          el.href = "#";
          el.innerHTML = i;

          if (i===pagination.current) {
              el.className = 'on';
          } else {
              el.onclick = (function(i) {
                  return function() {
                      pagination.gotoPage(i);
                  }
              })(i);
          }
  
          fragment.appendChild(el);
      }
      paginationEl.appendChild(fragment);
  }
  
  // 검색결과 목록 또는 마커를 클릭했을 때 호출되는 함수입니다
  // 인포윈도우에 장소명을 표시합니다
  function displayInfowindow(marker, title, urls) {
      var content = '<div style="padding:5px;z-index:1;">' + title + '</div>';
    
      infowindow.value.setContent(content);
      infowindow.value.open(map.value, marker);
  }
  
   // 검색결과 목록의 자식 Element를 제거하는 함수입니다
  function removeAllChildNods(el) {   
      while (el.hasChildNodes()) {
          el.removeChild (el.lastChild);
      }
  }


const store = useCounterStore()

const selectLocal1 = ref(Object.keys(local)[0])
const selectLocal2 = ref(Object.keys(local[selectLocal1.value])[0])
const selectLocal3 = ref(local[selectLocal1.value][selectLocal2.value][0])

const localType1 = ref(Object.keys(local))
const localType2 = computed(() => {
  return Object.keys(local[selectLocal1.value])
})
const localType3 = computed(() => {
  return local[selectLocal1.value][selectLocal2.value]
})


const banks = ["은행선택","국민은행","우리은행","신한은행","KEB하나은행","한국스탠다드차타드은행","외한은행","한국시티은행","경남은행","광주은행","대구은행","부산은행","전북은행","제주은행","기업은행","농협","수협","한국산업은행","한국수출입은행"]
const selectedBank = ref(banks[0])

// console.log(region)
</script>