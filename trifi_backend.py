from flask import Flask, request, jsonify
from trifi_learn import TriFiLearn
import math

app = Flask(__name__)

tfl = TriFiLearn()

DEFAULT_FEATURE = 180
# routers for the 10th floor in lexicographical order
KNOWN_ROUTERS = ["00:11:45:20:0c:00",
                "00:14:a5:93:ad:18",
                "08:ea:44:91:2e:54",
                "08:ea:44:91:2e:55",
                "08:ea:44:91:2e:6a",
                "08:ea:44:9c:ed:68",
                "08:ea:44:9c:ed:69",
                "08:ea:44:9c:ed:6a",
                "08:ea:44:9c:ed:6b",
                "08:ea:44:9c:ed:d4",
                "08:ea:44:9c:ed:d5",
                "08:ea:44:9c:ed:d6",
                "08:ea:44:9c:ed:e8",
                "08:ea:44:9c:ed:e9",
                "08:ea:44:9c:ed:ea",
                "08:ea:44:9c:ed:eb",
                "08:ea:44:9c:ee:14",
                "08:ea:44:9c:ee:15",
                "08:ea:44:9c:ee:16",
                "08:ea:44:9c:ee:28",
                "08:ea:44:9c:ee:29",
                "08:ea:44:9c:ee:2a",
                "08:ea:44:9c:ee:2b",
                "0e:18:1a:04:41:d2",
                "10:0d:7f:c7:38:bd",
                "10:0d:7f:d1:e9:91",
                "10:0d:7f:d2:32:31",
                "10:0d:7f:d2:f8:66",
                "10:0d:7f:d5:bb:f7",
                "24:a2:e1:ed:5c:0a",
                "24:c9:a1:13:4a:fc",
                "24:c9:a1:13:4d:c8",
                "24:c9:a1:13:4e:28",
                "24:c9:a1:13:4e:98",
                "24:c9:a1:13:4f:28",
                "24:c9:a1:13:4f:2c",
                "24:c9:a1:16:d1:28",
                "24:c9:a1:53:4d:c8",
                "24:c9:a1:53:4e:28",
                "24:c9:a1:53:4e:98",
                "24:c9:a1:53:4f:28",
                "24:c9:a1:53:4f:2c",
                "24:c9:a1:53:50:b8",
                "24:c9:a1:56:d1:23",
                "24:c9:a1:56:d1:28",
                "24:c9:a1:93:4a:f8",
                "24:c9:a1:93:4a:fc",
                "24:c9:a1:93:4b:18",
                "24:c9:a1:93:4d:c8",
                "24:c9:a1:93:4e:28",
                "24:c9:a1:93:4e:98",
                "24:c9:a1:93:4f:28",
                "24:c9:a1:93:4f:2c",
                "24:c9:a1:96:d1:28",
                "24:de:c6:36:3e:40",
                "24:de:c6:a5:fd:88",
                "24:de:c6:a6:04:30",
                "24:de:c6:a6:04:31",
                "24:de:c6:a6:04:32",
                "24:de:c6:a6:04:38",
                "24:de:c6:a6:04:39",
                "24:de:c6:a6:04:3a",
                "24:de:c6:a6:04:70",
                "24:de:c6:a6:04:71",
                "24:de:c6:a6:04:72",
                "24:de:c6:a6:04:78",
                "24:de:c6:a6:04:79",
                "24:de:c6:a6:04:7a",
                "24:de:c6:a6:07:c0",
                "24:de:c6:a6:07:c1",
                "24:de:c6:a6:07:c2",
                "24:de:c6:a6:07:c8",
                "24:de:c6:a6:07:c9",
                "24:de:c6:a6:07:ca",
                "24:de:c6:a6:07:f0",
                "24:de:c6:a6:07:f1",
                "24:de:c6:a6:07:f2",
                "24:de:c6:a6:07:f8",
                "24:de:c6:a6:07:f9",
                "24:de:c6:a6:07:fa",
                "24:de:c6:a6:08:b0",
                "24:de:c6:a6:08:b1",
                "24:de:c6:a6:08:b2",
                "24:de:c6:a6:08:b8",
                "24:de:c6:a6:08:b9",
                "24:de:c6:a6:08:ba",
                "24:de:c6:a6:09:70",
                "24:de:c6:a6:09:71",
                "24:de:c6:a6:09:72",
                "24:de:c6:a6:09:78",
                "24:de:c6:a6:09:79",
                "24:de:c6:a6:09:7a",
                "28:cf:da:ad:b4:c1",
                "2a:28:5d:2c:dd:c0",
                "2a:cf:da:ad:b4:c2",
                "2c:9e:fc:c8:7e:a2",
                "2c:b0:5d:9c:ea:08",
                "40:8b:07:4b:6b:28",
                "50:46:5d:d2:42:a8",
                "54:3d:37:a4:3d:78",
                "6c:f3:7f:d3:85:00",
                "6c:f3:7f:d3:d3:60",
                "6c:f3:7f:d4:f0:80",
                "74:d0:2b:85:f3:c8",
                "74:d0:2b:85:f3:cc",
                "90:72:40:13:70:aa",
                "bc:ee:7b:de:4f:00",
                "bc:ee:7b:de:4f:01",
                "d8:c7:c8:03:fa:60",
                "e0:1c:41:04:97:d4",
                "e0:1c:41:04:97:d5",
                "e0:1c:41:04:97:e8",
                "e0:1c:41:04:97:e9",
                "e0:1c:41:04:97:ea",
                "e0:1c:41:04:99:28",
                "e0:1c:41:04:99:29",
                "e0:1c:41:04:99:2a",
                "e0:1c:41:04:99:54",
                "e0:1c:41:04:99:55",
                "e0:1c:41:04:99:68",
                "e0:1c:41:04:99:69",
                "e0:1c:41:04:99:6a",
                "e0:1c:41:04:99:d4",
                "e0:1c:41:04:99:d5",
                "e0:1c:41:04:99:e8",
                "e0:1c:41:04:99:e9",
                "e0:1c:41:04:99:ea",
                "e0:1c:41:04:a9:28",
                "e0:1c:41:04:a9:29",
                "e0:1c:41:04:a9:2a",
                "e0:1c:41:04:a9:e8",
                "e0:1c:41:04:a9:e9",
                "e0:1c:41:04:a9:ea"]


# predict endpoint takes a router signature json from the trifi executable
# and returns an x, y location
@app.route('/predict', methods=['POST', 'GET']) # TODO: change this to just GET
def predict():
    data = request.get_json()
    routers = data['routers']
    features = getFeaturesFromRouters(routers)
    loc = {
	   'x': tfl.predictX(features),
	   'y': tfl.predictY(features)
    }
	
    return jsonify(loc)

# training endpoint to update the training set with new data
@app.route('/train', methods=['PUT'])
def train():
    data = request.get_json()
    routerSignature = data['routerSignature']
    routers = data['routers']
    features = getFeaturesFromRouters(routers)
    location = data['location']
    x = location['x']
    y = location['y']

    tfl.trainX(x, features)
    tfl.trainY(y, features)


# iter through router json and extract features for each
def getFeaturesFromRouters(routers):
    features = []
    for knownRouter in KNOWN_ROUTERS:
        try:
            thisRouter = routers[knownRouter]
            features.append(getFeatureFromRouter(thisRouter))
        except KeyError:
            features.append(DEFAULT_FEATURE)

    return features

# applies distance formula to router information to get a feature
def getFeatureFromRouter(router):
    strength = router['strength']
    frequency = router['frequency']
    feature = 10 ** ((27.55 - (20 * math.log10(frequency)) - strength) / 20)
    return "{:.3f}".format(feature)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()








