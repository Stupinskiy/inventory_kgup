from django.db import models


class House(models.Model):
    address = models.CharField(max_length=255)
    year_built = models.IntegerField()
    floors = models.IntegerField()
    wall_material = models.CharField(max_length=100)
    total_area = models.FloatField()
    living_area = models.FloatField()
    apartments_count = models.IntegerField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.address


class Apartment(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)
    floor = models.IntegerField()
    total_area = models.FloatField()
    living_area = models.FloatField()
    rooms = models.IntegerField()
    registered_people = models.IntegerField(default=0)
    ownership_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.house.address} — кв. {self.number}"


class ApartmentEquipment(models.Model):
    apartment = models.OneToOneField(Apartment, on_delete=models.CASCADE)
    gas = models.BooleanField(default=False)
    water = models.BooleanField(default=False)
    sewage = models.BooleanField(default=False)
    electricity_meter = models.BooleanField(default=False)
    water_meter = models.BooleanField(default=False)
    heating = models.CharField(max_length=100)
    balcony = models.BooleanField(default=False)
    bathroom_type = models.CharField(max_length=100)
    networks_condition = models.CharField(max_length=255)


class CommissionMember(models.Model):
    year = models.IntegerField()
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.year} — {self.full_name}"


class InventoryAct(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    year = models.IntegerField()
    inspection_date = models.DateField()
    technical_condition = models.TextField()
    remarks = models.TextField(blank=True, null=True)
    conclusion = models.TextField()
    inspector = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
