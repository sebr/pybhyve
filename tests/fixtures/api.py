"""Define fixtures for testing the REST API."""
import pytest

@pytest.fixture()
def devices_json():
    """Define a response to /v1/devices."""
    return [
  {
    "last_connected_at": "2019-12-16T01:35:52.971Z",
    "address": {
    },
    "firmware_version": "0030",
    "name": "Home",
    "type": "bridge",
    "battery": None,
    "image_url": "https://s3-us-west-2.amazonaws.com/orbit-irrigation/device-assets/test",
    "updated_at": "2019-12-16T01:35:52.972Z",
    "reference": "11672220399e",
    "mac_address": "11672220399e",
    "mesh_id": "3ae4be339f0c72d7d332b82b",
    "status": {
      "next_start_time": "1970-01-01T00:00:00+11:00",
      "next_start_programs": [],
      "watering_status": None
    },
    "wifi_version": 0,
    "id": "12345",
    "num_stations": 0,
    "user_id": "98765",
    "notified_disconnected_at": "2019-07-27T00:18:53.770Z",
    "device_gateway_topic": "devices-2",
    "hardware_version": "BH1-0001",
    "is_connected": True,
    "created_at": "2019-04-28T00:21:04.890Z"
  },
  {
    "last_connected_at": "2019-12-16T01:35:52.974Z",
    "water_sense_mode": "auto",
    "firmware_version": "0041",
    "name": "Lawn",
    "type": "sprinkler_timer",
    "manual_preset_runtime_sec": 1200,
    "battery": { "percent": 50, "charging": None },
    "restricted_frequency": {
      "type": "days",
      "days": [1, 2, 3, 4, 5],
      "restricted_times": []
    },
    "weather_delay_thresholds": {
      "precip_prob": 30,
      "precip_in": 0.125,
      "wind_speed_mph": 20,
      "freeze_temp_f": 37
    },
    "updated_at": "2019-12-17T06:10:31.764Z",
    "reference": "11672220399e-7306",
    "mac_address": "3367881000a8",
    "mesh_id": "3ae4be339f0c72d7d332b82b",
    "status": {
      "run_mode": "auto",
      "next_start_programs": [],
      "rain_delay_overridden_at": "2018-05-10T19:19:52.199Z",
      "watering_status": None,
      "rain_delay": 0,
      "flow_sensor": None,
      "next_start_time": "2019-12-19T07:30:00+11:00",
      "rain_delay_started_at": "2019-12-17T05:19:06.000Z"
    },
    "id": "5ae3c7884f0c72d7d626ba06",
    "num_stations": 1,
    "zones": [
      {
        "station": 1,
        "slope_grade": 0,
        "sun_shade": "full_sun",
        "name": "Backyard",
        "landscape_type": "warm_season_turf",
        "geometry": {
          "type": "arc",
          "radius": 14.040322303771973,
          "geometry": 187.47169494628906
        },
        "image_url": "https://s3-us-west-2.amazonaws.com/orbit-irrigation/zone-assets/5ae3be204f0c72d7d626b811/test",
        "num_sprinklers": 1,
        "soil_type": "loam",
        "catch_cup_volumes": [],
        "catch_cup_run_time": 0,
        "smart_watering_enabled": True,
        "sprinkler_type": "impact"
      }
    ],
    "user_id": "98765",
    "notified_disconnected_at": "2019-11-16T13:42:22.668Z",
    "device_gateway_topic": "devices-2",
    "hardware_version": "HT25-0000",
    "is_connected": True,
    "created_at": "2019-04-28T00:59:52.048Z",
    "suggested_start_time": "07:30",
  }]
