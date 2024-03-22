from flask import Flask, request, jsonify
from astropy.cosmology import FlatLambdaCDM
import astropy.units as u

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate_distance():
    # Extracting arcseconds and redshift from the POST request
    data = request.json
    arcsec = data.get('arcsec', 0)
    redshift = data.get('redshift', 0)

    # Define your cosmology (Hubble constant and matter density)
    cosmo = FlatLambdaCDM(H0=70, Om0=0.3)

    # Calculation
    ang_distance_mpc = cosmo.angular_diameter_distance(redshift)
    ang_size_rad = (arcsec * u.arcsec).to(u.rad).value
    distance_parsecs = (ang_distance_mpc.to(u.pc) * ang_size_rad).value

    return jsonify(distance_parsecs=distance_parsecs)

if __name__ == '__main__':
    app.run(debug=True)
