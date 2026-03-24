from flask import *
from bs4 import BeautifulSoup
import requests
import json

app = Flask(__name__)

@app.route('/' , methods=['GET']    )
def home():
    #url1 = request.args.get('url1')
    page = request.args.get('page')
    make= request.args.get('make')
    site = request.args.get('site')
    model = request.args.get('model')
    buy_now = request.args.get('buy_now')
    transmission = request.args.get('transmission')
    fuel = request.args.get('fuel')
    status = request.args.get('status')
    drive = request.args.get('drive')
    damage_pr = request.args.get('damage_pr')
    document = request.args.get('document')
    engine = request.args.get('engine')
    year = request.args.get('year')
    odometer= request.args.get('odometer')


    url1 = (f"https://car-link.tools/search")
    prams = {"make": {make},"site": {site},"model": {model},"buy_now": {buy_now},"page": {page},"transmission": {transmission},"fuel": {fuel},"status": {status},"drive": {drive},"damage_pr": {damage_pr},"document": {document},"engine": {engine},"year": {year},"odometer": {odometer}}

    url1 = requests.get(url1, params=prams)

    car_lots = []
    src = url1.content
    cc = src.decode('utf-8')
    items = BeautifulSoup(cc).find_all("script")
    num = len(items)
    cc=[]
    
    for i in range(num):
        car_detal = items[i].text
        if "content_item__qId8i" in car_detal and i > 0 and  "lot_id" in car_detal:
            
            item =items[i].text.replace(R"\"", "")
            id1 = item.split('data:{id:')[1]
            id1 = id1.split(",lot_id:")[0]
            lot_id = item.split("lot_id:")[1]
            lot_id = int(lot_id.split(",")[0])
            site = item.split("site:")[1]
            site = int(site.split(",")[0])
            base_site = item.split("base_site:")[1]
            base_site = base_site.split(",")[0]
            salvage_id = item.split("salvage_id:")[1]
            salvage_id = salvage_id.split(",")[0]
            odometer = item.split("odometer:")[1]
            odometer = int(odometer.split(",")[0])
            if "current_bid:" in item:
                current_bid = item.split("current_bid:")[1]
                current_bid = current_bid.split(",")[0]
            else:
                current_bid = 0
            price_new = item.split("price_new:")[1]
            price_new = price_new.split(",")[0]
            price_future = item.split("price_future:")[1]
            price_future = price_future.split(",")[0]
            if "price_reserve:" in item:
                price_reserve = item.split("price_reserve:")[1]
                price_reserve = price_reserve.split(",")[0]
            else:
                price_reserve = 0
            auction_date = item.split("auction_date:")[1]
            auction_date = auction_date.split(",")[0]
            cost_priced = item.split("cost_priced:")[1]
            cost_priced = cost_priced.split(",")[0]
            cost_repair = item.split("cost_repair:")[1]
            cost_repair = cost_repair.split(",")[0]
            year = item.split("year:")[1]
            year = year.split(",")[0]
            cylinders = item.split("cylinders:")[1]
            cylinders = cylinders.split(",")[0]
            state = item.split("state:")[1]
            state = state.split(",")[0]
            vehicle_type = item.split("vehicle_type:")[1]
            vehicle_type = vehicle_type.split(",")[0]
            auction_type = item.split("auction_type:")[1]
            auction_type = auction_type.split(",")[0]
            make = item.split("make:")[1]
            make = make.split(",")[0]
            if "model:" in item:
                model = item.split("model:")[1]
                model = model.split(",")[0]
            else:
                model = "null"
            if "series:" in item:
                 series = item.split("series:")[1]
                 series = series.split(",")[0]
            else:
                series = "null"
            damage_pr = item.split("damage_pr:")[1]
            damage_pr = damage_pr.split(",")[0]
            damage_sec = item.split("damage_sec:")[1]
            damage_sec = damage_sec.split(",")[0]
            keys = item.split("keys:")[1]
            keys = keys.split(",")[0]
            odobrand = item.split("odobrand:")[1]
            odobrand = odobrand.split(",")[0]
            drive = item.split("drive:")[1]
            drive = drive.split(",")[0]
            fuel = item.split("fuel:")[1]
            fuel = fuel.split(",")[0]
            transmission = item.split("transmission:")[1]
            transmission = transmission.split(",")[0]
            color = item.split("color:")[1]
            color = color.split(",")[0]
            status = item.split("status:")[1]
            status = status.split(",")[0]
            presale_status = item.split("presale_status:")[1]
            presale_status = presale_status.split(",")[0]
            title = item.split("title:")[1]
            title = title.split(",")[0]
            vin = item.split("vin:")[1]
            vin = vin.split(",")[0]
            if "engine:" in item:
                engine = item.split("engine:")[1]
                engine = engine.split(",")[0]
            else:
                engine = "null"
            if "engine_size:" in item:
                engine_size = item.split("engine_size:")[1]
                engine_size = engine_size.split(",")[0]
            else:
                engine_size = "null"
            location = item.split("location:")[1]
            location = location.split(",")[0]
            country = item.split("country:")[1]
            country= country.split(",")[0]
            document = item.split("document:")[1]
            document = document.split(",")[0]
            currency = item.split("currency:")[1]
            currency = currency.split(",")[0]
            is_buynow = item.split("is_buynow:")[1]
            is_buynow = is_buynow.split(",")[0]
            iaai_360 = item.split("iaai_360:")[1]
            iaai_360= iaai_360.split(",")[0]
            copart_exterior_360 = item.split("copart_exterior_360:")[1]
            copart_exterior_360 = copart_exterior_360.split(",")[0]
            copart_interior_360 = item.split("copart_interior_360:")[1]
            copart_interior_360 = copart_interior_360.split(",")[0]
            video = item.split("video:")[1]
            video = video.split(",")[0]
            link_img_hd= item.split("link_img_hd:[")[1]
            link_img_hd= link_img_hd.split(",")
            del link_img_hd[len(link_img_hd)-1]

            link_img_small = item.split("link_img_small:[")[1]
            link_img_small = link_img_small.split(",")
            del link_img_small[len(link_img_small)-1]

            is_offsite= item.split("is_offsite:")[1]
            is_offsite = is_offsite.split(",")[0]
            location_offsite = item.split("location_offsite:")[1]
            location_offsite = location_offsite.split(",")[0]
            link = item.split("link:")[1]
            link = link.split(",")[0]
            body_type = item.split("body_type:")[1]
            body_type = body_type.split(",")[0]
            seller_type = item.split("seller_type:")[1]
            seller_type = seller_type.split(",")[0]
            vehicle_score = item.split("vehicle_score:")[1]
            vehicle_score = vehicle_score.split(",")[0]
            created_at = item.split("created_at:")[1]
            created_at = created_at.split("created_at:")[0]
            updated_at = item.split("updated_at:")[1]
            updated_at = updated_at.split(",")[0]
            data = {"id":id1,"lot_id":lot_id,"site":site,"base_site":base_site,"salvage_id":salvage_id,"odometer":odometer,"current_bid":current_bid,"price_new":price_new,"price_future":price_future,"price_reserve":price_reserve,"auction_date":auction_date,"cost_priced":cost_priced,"cost_repair":cost_repair,"year":year,"cylinders":cylinders,"state":state,"vehicle_type":vehicle_type,"auction_type":auction_type,"make":make,"model":model,"series":series,"damage_pr":damage_pr,"damage_sec":damage_sec,"keys":keys,"odobrand":odobrand,"drive":drive,"fuel":fuel,"transmission":transmission,"color":color,"status":status,"presale_status":presale_status,"title":title,"vin":vin,"engine":engine,"engine_size":engine_size,"location":location,"country":country,"document":document,"currency":currency,"is_buynow":is_buynow,"iaai_360":iaai_360,"copart_exterior_360":copart_exterior_360,
                    "copart_interior_360":copart_interior_360, "video":video, "link_img_hd ":link_img_hd, "link_img_small ":link_img_small, "is_offsite ":is_offsite, "location_offsite ":location_offsite, "link ":link, "body_type ":body_type, "seller_type ":seller_type, "vehicle_score ":vehicle_score, "created_at ":created_at, "updated_at ":updated_at}
            car_lots.append(data)
                

    return jsonify(car_lots)

@app.route('/history' , methods=['GET'] )
def cool():

    url2 = (f"https://car-link.tools/search?page=7&size=10&site=2")
    url2 = requests.get(url2)
    history_lot = []



if __name__ == '__main__':
    app.run(debug=True)            if "current_bid:" in item:
                current_bid = item.split("current_bid:")[1]
                current_bid = current_bid.split(",")[0]
            else:
                current_bid = 0
            price_new = item.split("price_new:")[1]
            price_new = price_new.split(",")[0]
            price_future = item.split("price_future:")[1]
            price_future = price_future.split(",")[0]
            if "price_reserve:" in item:
                price_reserve = item.split("price_reserve:")[1]
                price_reserve = price_reserve.split(",")[0]
            else:
                price_reserve = 0
            auction_date = item.split("auction_date:")[1]
            auction_date = auction_date.split(",")[0]
            cost_priced = item.split("cost_priced:")[1]
            cost_priced = cost_priced.split(",")[0]
            cost_repair = item.split("cost_repair:")[1]
            cost_repair = cost_repair.split(",")[0]
            year = item.split("year:")[1]
            year = year.split(",")[0]
            cylinders = item.split("cylinders:")[1]
            cylinders = cylinders.split(",")[0]
            state = item.split("state:")[1]
            state = state.split(",")[0]
            vehicle_type = item.split("vehicle_type:")[1]
            vehicle_type = vehicle_type.split(",")[0]
            auction_type = item.split("auction_type:")[1]
            auction_type = auction_type.split(",")[0]
            make = item.split("make:")[1]
            make = make.split(",")[0]
            if "model:" in item:
                model = item.split("model:")[1]
                model = model.split(",")[0]
            else:
                model = "null"
            if "series:" in item:
                 series = item.split("series:")[1]
                 series = series.split(",")[0]
            else:
                series = "null"
            damage_pr = item.split("damage_pr:")[1]
            damage_pr = damage_pr.split(",")[0]
            damage_sec = item.split("damage_sec:")[1]
            damage_sec = damage_sec.split(",")[0]
            keys = item.split("keys:")[1]
            keys = keys.split(",")[0]
            odobrand = item.split("odobrand:")[1]
            odobrand = odobrand.split(",")[0]
            drive = item.split("drive:")[1]
            drive = drive.split(",")[0]
            fuel = item.split("fuel:")[1]
            fuel = fuel.split(",")[0]
            transmission = item.split("transmission:")[1]
            transmission = transmission.split(",")[0]
            color = item.split("color:")[1]
            color = color.split(",")[0]
            status = item.split("status:")[1]
            status = status.split(",")[0]
            presale_status = item.split("presale_status:")[1]
            presale_status = presale_status.split(",")[0]
            title = item.split("title:")[1]
            title = title.split(",")[0]
            vin = item.split("vin:")[1]
            vin = vin.split(",")[0]
            if "engine:" in item:
                engine = item.split("engine:")[1]
                engine = engine.split(",")[0]
            else:
                engine = "null"
            if "engine_size:" in item:
                engine_size = item.split("engine_size:")[1]
                engine_size = engine_size.split(",")[0]
            else:
                engine_size = "null"
            location = item.split("location:")[1]
            location = location.split(",")[0]
            country = item.split("country:")[1]
            country= country.split(",")[0]
            document = item.split("document:")[1]
            document = document.split(",")[0]
            currency = item.split("currency:")[1]
            currency = currency.split(",")[0]
            is_buynow = item.split("is_buynow:")[1]
            is_buynow = is_buynow.split(",")[0]
            iaai_360 = item.split("iaai_360:")[1]
            iaai_360= iaai_360.split(",")[0]
            copart_exterior_360 = item.split("copart_exterior_360:")[1]
            copart_exterior_360 = copart_exterior_360.split(",")[0]
            copart_interior_360 = item.split("copart_interior_360:")[1]
            copart_interior_360 = copart_interior_360.split(",")[0]
            video = item.split("video:")[1]
            video = video.split(",")[0]
            link_img_hd= item.split("link_img_hd:[")[1]
            link_img_hd= link_img_hd.split(",")
            del link_img_hd[len(link_img_hd)-1]

            link_img_small = item.split("link_img_small:[")[1]
            link_img_small = link_img_small.split(",")
            del link_img_small[len(link_img_small)-1]

            is_offsite= item.split("is_offsite:")[1]
            is_offsite = is_offsite.split(",")[0]
            location_offsite = item.split("location_offsite:")[1]
            location_offsite = location_offsite.split(",")[0]
            link = item.split("link:")[1]
            link = link.split(",")[0]
            body_type = item.split("body_type:")[1]
            body_type = body_type.split(",")[0]
            seller_type = item.split("seller_type:")[1]
            seller_type = seller_type.split(",")[0]
            vehicle_score = item.split("vehicle_score:")[1]
            vehicle_score = vehicle_score.split(",")[0]
            created_at = item.split("created_at:")[1]
            created_at = created_at.split("created_at:")[0]
            updated_at = item.split("updated_at:")[1]
            updated_at = updated_at.split(",")[0]
            data = {"id":id1,"lot_id":lot_id,"site":site,"base_site":base_site,"salvage_id":salvage_id,"odometer":odometer,"current_bid":current_bid,"price_new":price_new,"price_future":price_future,"price_reserve":price_reserve,"auction_date":auction_date,"cost_priced":cost_priced,"cost_repair":cost_repair,"year":year,"cylinders":cylinders,"state":state,"vehicle_type":vehicle_type,"auction_type":auction_type,"make":make,"model":model,"series":series,"damage_pr":damage_pr,"damage_sec":damage_sec,"keys":keys,"odobrand":odobrand,"drive":drive,"fuel":fuel,"transmission":transmission,"color":color,"status":status,"presale_status":presale_status,"title":title,"vin":vin,"engine":engine,"engine_size":engine_size,"location":location,"country":country,"document":document,"currency":currency,"is_buynow":is_buynow,"iaai_360":iaai_360,"copart_exterior_360":copart_exterior_360,
                    "copart_interior_360":copart_interior_360, "video":video, "link_img_hd ":link_img_hd, "link_img_small ":link_img_small, "is_offsite ":is_offsite, "location_offsite ":location_offsite, "link ":link, "body_type ":body_type, "seller_type ":seller_type, "vehicle_score ":vehicle_score, "created_at ":created_at, "updated_at ":updated_at}
            car_lots.append(data)
                

    return jsonify(car_lots)

@app.route('/history' , methods=['GET'] )
def cool():

    url2 = (f"https://car-link.tools/search?page=7&size=10&site=2")
    url2 = requests.get(url2)
    history_lot = []



if __name__ == '__main__':
    app.run(debug=True)
