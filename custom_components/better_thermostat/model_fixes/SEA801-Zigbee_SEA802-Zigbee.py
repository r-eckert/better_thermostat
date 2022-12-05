def fix_local_calibration(self, entity_id, offset):
    # device SEA802 fix
    if offset > -1.5:
        offset -= 1.5
    return offset


def fix_target_temperature_calibration(self, entity_id, temperature):
    # device SEA802 fix
    _cur_trv_temp = float(
        self.hass.states.get(entity_id).attributes["current_temperature"]
    )
    if _cur_trv_temp is None:
        return temperature
    if temperature - _cur_trv_temp < 1.5:
        temperature += 1.5
    return temperature
