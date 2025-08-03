from datetime import datetime, timedelta


class ReservationSystem:
    def __init__(self):
        self.reservations = {}
        self.tables = {
            'small': [1, 2, 3, 4],
            'medium': [5, 6, 7, 8],
            'large': [9, 10]
        }

    def make_reservation(self, name, guests, time_slot):
        table_type = self._determine_table_type(guests)
        available = self._check_availability(table_type, time_slot)

        if available:
            res_id = len(self.reservations) + 1
            self.reservations[res_id] = {
                'name': name,
                'guests': guests,
                'time': time_slot,
                'table': available[0],
                'status': 'confirmed'
            }
            return res_id
        return None

    def _determine_table_type(self, guests):
        if guests <= 2:
            return 'small'
        elif guests <= 4:
            return 'medium'
        else:
            return 'large'

    def _check_availability(self, table_type, time_slot):
        reserved_tables = [
            r['table'] for r in self.reservations.values()
            if r['time'] == time_slot and r['status'] == 'confirmed'
        ]
        available = [t for t in self.tables[table_type] if t not in reserved_tables]
        return available if available else None

    def get_reservations(self, date=None):
        if date:
            return {k: v for k, v in self.reservations.items() if v['time'].date() == date}
        return self.reservations