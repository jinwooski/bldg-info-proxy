from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/building-info", methods=["GET"])
def get_building_info():
    sigunguCd = "11680"
    bjdongCd = "10300"
    platGbCd = "0"
    bun = "0123"
    ji = "0045"

    api_key = "ZDZZacnyq8C2p4qJOiFMsxbZPDMqNY/8+/9AHHzueYIv32i4ttdfpznV8b7lrbehDj+K1gGEt1dwD5nQ6glx4A=="
    url = f"https://apis.data.go.kr/1613000/BldRgstService_v2/getBrTitleInfo"
    params = {
        "serviceKey": api_key,
        "sigunguCd": sigunguCd,
        "bjdongCd": bjdongCd,
        "platGbCd": platGbCd,
        "bun": bun,
        "ji": ji,
        "_type": "json"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        item = data["response"]["body"]["items"]["item"][0]

        return jsonify({
            "area": item["totArea"],
            "usage": item["mainPurpsCdNm"],
            "structure": item["strctCdNm"]
        }), 200, {
            "Access-Control-Allow-Origin": "*"
        }

    except Exception as e:
        return jsonify({"error": str(e)}), 500, {
            "Access-Control-Allow-Origin": "*"
        }

if __name__ == "__main__":
    app.run()
