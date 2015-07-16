# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class MiCustomers(models.Model):
    newdata = models.IntegerField(blank=True, null=True)
    facilityid = models.CharField(max_length=20, blank=True, null=True)
    fcustcode = models.CharField(max_length=20, blank=True, null=True)
    fcompany = models.CharField(max_length=50, blank=True, null=True)
    fcfname = models.CharField(max_length=50, blank=True, null=True)
    fclname = models.CharField(max_length=50, blank=True, null=True)
    faddr1 = models.CharField(max_length=50, blank=True, null=True)
    faddr2 = models.CharField(max_length=50, blank=True, null=True)
    fcity = models.CharField(max_length=50, blank=True, null=True)
    fstate = models.CharField(max_length=50, blank=True, null=True)
    fzip = models.CharField(max_length=50, blank=True, null=True)
    fphone = models.CharField(max_length=50, blank=True, null=True)
    ffax = models.CharField(max_length=50, blank=True, null=True)
    fcusttype = models.CharField(max_length=50, blank=True, null=True)
    fcreditlim = models.CharField(max_length=50, blank=True, null=True)
    fservrep = models.CharField(max_length=50, blank=True, null=True)
    fbaddr1 = models.CharField(max_length=50, blank=True, null=True)
    fbaddr2 = models.CharField(max_length=50, blank=True, null=True)
    fbcity = models.CharField(max_length=50, blank=True, null=True)
    fbstate = models.CharField(max_length=50, blank=True, null=True)
    fbzip = models.CharField(max_length=50, blank=True, null=True)
    fcomment = models.CharField(max_length=50, blank=True, null=True)
    fhold = models.CharField(max_length=50, blank=True, null=True)
    fbroker = models.CharField(max_length=50, blank=True, null=True)
    funiqsale = models.CharField(max_length=50, blank=True, null=True)
    funiqsalby = models.CharField(max_length=50, blank=True, null=True)
    funiqpo = models.CharField(max_length=50, blank=True, null=True)
    funiqpoby = models.CharField(max_length=50, blank=True, null=True)
    fbillpal = models.CharField(max_length=50, blank=True, null=True)
    fcommitby = models.CharField(max_length=50, blank=True, null=True)
    funearnper = models.CharField(max_length=50, blank=True, null=True)
    fisdist = models.CharField(max_length=50, blank=True, null=True)
    fdistcarr = models.CharField(max_length=50, blank=True, null=True)
    fdisttran = models.CharField(max_length=50, blank=True, null=True)
    fdistcube = models.CharField(max_length=50, blank=True, null=True)
    fdocinchrg = models.CharField(max_length=50, blank=True, null=True)
    fgldocin = models.CharField(max_length=50, blank=True, null=True)
    fdocoutchg = models.FloatField(blank=True, null=True)
    fgldocout = models.FloatField(blank=True, null=True)
    fdoclotchg = models.FloatField(blank=True, null=True)
    fgldoclot = models.FloatField(blank=True, null=True)
    fdelwgtbrk = models.FloatField(blank=True, null=True)
    fmininvchg = models.FloatField(blank=True, null=True)
    ffulpalchg = models.FloatField(blank=True, null=True)
    fglfulpal = models.FloatField(blank=True, null=True)
    fcsepckchg = models.FloatField(blank=True, null=True)
    fglcsepick = models.FloatField(blank=True, null=True)
    flinechrg = models.FloatField(blank=True, null=True)
    fgllinechg = models.FloatField(blank=True, null=True)
    fbolreport = models.CharField(max_length=100, blank=True, null=True)
    fwrreport = models.CharField(max_length=100, blank=True, null=True)
    finvreport = models.CharField(max_length=100, blank=True, null=True)
    fpikreport = models.CharField(max_length=100, blank=True, null=True)
    fbilreport = models.CharField(max_length=100, blank=True, null=True)
    finvcrept = models.CharField(max_length=100, blank=True, null=True)
    fincwrept = models.CharField(max_length=100, blank=True, null=True)
    foutcwrept = models.CharField(max_length=100, blank=True, null=True)
    fcredrept = models.CharField(max_length=100, blank=True, null=True)
    fchckrept = models.CharField(max_length=100, blank=True, null=True)
    fraternwl = models.CharField(max_length=100, blank=True, null=True)
    favgbiling = models.CharField(max_length=100, blank=True, null=True)
    fwho = models.CharField(max_length=100, blank=True, null=True)
    fdatestamp = models.CharField(max_length=100, blank=True, null=True)
    fmatprod = models.CharField(max_length=100, blank=True, null=True)
    fmatchday = models.CharField(max_length=100, blank=True, null=True)
    fusepick = models.CharField(max_length=100, blank=True, null=True)
    fcube = models.CharField(max_length=100, blank=True, null=True)
    fcubewgt = models.CharField(max_length=100, blank=True, null=True)
    fcfullpart = models.CharField(max_length=100, blank=True, null=True)
    fpaljack = models.CharField(max_length=100, blank=True, null=True)
    fovercube = models.CharField(max_length=100, blank=True, null=True)
    fmbolrept = models.CharField(max_length=100, blank=True, null=True)
    fonlypar = models.CharField(max_length=100, blank=True, null=True)
    fpalexch = models.CharField(max_length=100, blank=True, null=True)
    fstatus = models.CharField(max_length=100, blank=True, null=True)
    mailboxnme = models.CharField(max_length=100, blank=True, null=True)
    schedintim = models.CharField(max_length=100, blank=True, null=True)
    schedoutim = models.CharField(max_length=100, blank=True, null=True)
    ediconfcom = models.CharField(max_length=100, blank=True, null=True)
    confirmord = models.CharField(max_length=100, blank=True, null=True)
    active = models.CharField(max_length=100, blank=True, null=True)
    actdate = models.CharField(max_length=100, blank=True, null=True)
    tunnelseq = models.CharField(max_length=100, blank=True, null=True)
    fcomstatus = models.CharField(max_length=100, blank=True, null=True)
    fdwnstkchg = models.CharField(max_length=100, blank=True, null=True)
    fgldownstk = models.CharField(max_length=100, blank=True, null=True)
    fdownbill = models.CharField(max_length=100, blank=True, null=True)
    fgroupcode = models.CharField(max_length=100, blank=True, null=True)
    fusemetric = models.CharField(max_length=100, blank=True, null=True)
    fgetpalwgt = models.CharField(max_length=100, blank=True, null=True)
    fautowood = models.CharField(max_length=100, blank=True, null=True)
    fcustucc = models.CharField(max_length=100, blank=True, null=True)
    femail = models.CharField(max_length=100, blank=True, null=True)
    fcselyrchg = models.CharField(max_length=100, blank=True, null=True)
    fglcselyr = models.CharField(max_length=100, blank=True, null=True)
    fcountback = models.CharField(max_length=100, blank=True, null=True)
    fdrvrchek = models.CharField(max_length=100, blank=True, null=True)
    fbilltax = models.CharField(max_length=100, blank=True, null=True)
    floadnotes = models.CharField(max_length=100, blank=True, null=True)
    fsap_sto = models.CharField(max_length=100, blank=True, null=True)
    ftunstolod = models.CharField(max_length=100, blank=True, null=True)
    fcpbillopt = models.CharField(max_length=100, blank=True, null=True)
    fhpbasis = models.CharField(max_length=100, blank=True, null=True)
    fhprate = models.CharField(max_length=100, blank=True, null=True)
    fhpgl = models.CharField(max_length=100, blank=True, null=True)
    fhpbilltyp = models.CharField(max_length=100, blank=True, null=True)
    fhpwgttyp = models.CharField(max_length=100, blank=True, null=True)
    faoinvrept = models.CharField(max_length=100, blank=True, null=True)
    fbillprdgp = models.CharField(max_length=100, blank=True, null=True)
    ediconfin = models.CharField(max_length=100, blank=True, null=True)
    fmbolcommt = models.CharField(max_length=100, blank=True, null=True)
    ftunelcros = models.CharField(max_length=100, blank=True, null=True)
    custkey = models.CharField(primary_key=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'mi_customers'


class ShipmentMaster(models.Model):
    newdata = models.IntegerField(db_column='newData', blank=True, null=True)  # Field name made lowercase.
    facilityid = models.CharField(db_column='facilityId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fbatch = models.CharField(db_column='FBATCH', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fcustcode = models.CharField(db_column='FCUSTCODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    floadnum = models.CharField(db_column='FLOADNUM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ftrailer = models.CharField(db_column='FTRAILER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fdoor = models.CharField(db_column='FDOOR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fpurchord = models.CharField(db_column='FPURCHORD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fsalesord = models.CharField(db_column='FSALESORD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fshipment = models.CharField(db_column='FSHIPMENT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fcustbol = models.CharField(db_column='FCUSTBOL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fdropnum = models.IntegerField(db_column='FDROPNUM', blank=True, null=True)  # Field name made lowercase.
    fbdate = models.CharField(db_column='FBDATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    forgdeldte = models.CharField(db_column='FORGDELDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    factdeldte = models.CharField(db_column='FACTDELDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fshipstat = models.CharField(db_column='FSHIPSTAT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    finuse = models.CharField(db_column='FINUSE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fltime = models.CharField(db_column='FLTIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcrosscust = models.CharField(db_column='FCROSSCUST', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fconscode = models.CharField(db_column='FCONSCODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fconsignee = models.CharField(db_column='FCONSIGNEE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    faddress1 = models.CharField(db_column='FADDRESS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    faddress2 = models.CharField(db_column='FADDRESS2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcity = models.CharField(db_column='FCITY', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fstate = models.CharField(db_column='FSTATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    destzip = models.CharField(db_column='DestZip', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fphone = models.CharField(db_column='FPHONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fseal = models.CharField(db_column='FSEAL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    carrierid = models.CharField(db_column='CarrierID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcheckqty = models.FloatField(db_column='FCHECKQTY', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    totalcube = models.FloatField(db_column='TotalCube', blank=True, null=True)  # Field name made lowercase.
    fcomment = models.CharField(db_column='FCOMMENT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fnotes = models.CharField(db_column='FNOTES', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ftemp = models.CharField(db_column='FTEMP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ffronttemp = models.CharField(db_column='FFRONTTEMP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fmidtemp = models.CharField(db_column='FMIDTEMP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fbacktemp = models.CharField(db_column='FBACKTEMP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fpaymethod = models.CharField(db_column='FPAYMETHOD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ftranmeth = models.CharField(db_column='FTRANMETH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fmbol = models.CharField(db_column='FMBOL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpickprint = models.CharField(db_column='FPICKPRINT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ftrancust = models.CharField(db_column='FTRANCUST', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fbilldoc = models.CharField(db_column='FBILLDOC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffulpalbil = models.CharField(db_column='FFULPALBIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcsepckbil = models.CharField(db_column='FCSEPCKBIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    flnechrbil = models.CharField(db_column='FLNECHRBIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fexportcty = models.CharField(db_column='FEXPORTCTY', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscansttme = models.CharField(db_column='FSCANSTTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscanstdte = models.CharField(db_column='FSCANSTDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscanentme = models.CharField(db_column='FSCANENTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscanendte = models.CharField(db_column='FSCANENDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscanbatch = models.CharField(db_column='FSCANBATCH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscanstat = models.CharField(db_column='FSCANSTAT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    feditype = models.CharField(db_column='FEDITYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fedi = models.CharField(db_column='FEDI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fedisnddte = models.CharField(db_column='FEDISNDDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fedisndtme = models.CharField(db_column='FEDISNDTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    foedi = models.CharField(db_column='FOEDI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    foedisdte = models.CharField(db_column='FOEDISDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    foedistme = models.CharField(db_column='FOEDISTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpalexchng = models.CharField(db_column='FPALEXCHNG', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpalcond = models.CharField(db_column='FPALCOND', max_length=30, blank=True, null=True)  # Field name made lowercase.
    floadoptcd = models.CharField(db_column='FLOADOPTCD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdtecngrsn = models.CharField(db_column='FDTECNGRSN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcarcngrsn = models.CharField(db_column='FCARCNGRSN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fversion = models.CharField(db_column='FVERSION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpallets = models.CharField(db_column='FPALLETS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchep = models.CharField(db_column='FCHEP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    farrivedte = models.CharField(db_column='FARRIVEDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    farrivetme = models.CharField(db_column='FARRIVETME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fstartdte = models.CharField(db_column='FSTARTDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fstarttme = models.CharField(db_column='FSTARTTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffinishdte = models.CharField(db_column='FFINISHDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffinishtme = models.CharField(db_column='FFINISHTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolorder = models.CharField(db_column='FCOLORDER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolwhse = models.CharField(db_column='FCOLWHSE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolneq = models.CharField(db_column='FCOLNEQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolqa = models.CharField(db_column='FCOLQA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolother = models.CharField(db_column='FCOLOTHER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolcoment = models.CharField(db_column='FCOLCOMENT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzorder = models.CharField(db_column='FFRZORDER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzwhse = models.CharField(db_column='FFRZWHSE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzneq = models.CharField(db_column='FFRZNEQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzqa = models.CharField(db_column='FFRZQA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzother = models.CharField(db_column='FFRZOTHER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzcoment = models.CharField(db_column='FFRZCOMENT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdryorder = models.CharField(db_column='FDRYORDER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdrywhse = models.CharField(db_column='FDRYWHSE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdryneq = models.CharField(db_column='FDRYNEQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdryqa = models.CharField(db_column='FDRYQA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdryother = models.CharField(db_column='FDRYOTHER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdrycoment = models.CharField(db_column='FDRYCOMENT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fconfirmnm = models.CharField(db_column='FCONFIRMNM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    flivedrop = models.CharField(db_column='FLIVEDROP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fschcoment = models.CharField(db_column='FSCHCOMENT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fsignoutme = models.CharField(db_column='FSIGNOUTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fsignoudte = models.CharField(db_column='FSIGNOUDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdriver = models.CharField(db_column='FDRIVER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fplanned = models.CharField(db_column='FPLANNED', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fwho = models.CharField(db_column='FWHO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdatestamp = models.CharField(db_column='FDATESTAMP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ftimestamp = models.CharField(db_column='FTIMESTAMP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fwhoship = models.CharField(db_column='FWHOSHIP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fshipdate = models.CharField(db_column='FSHIPDATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fshiptime = models.CharField(db_column='FSHIPTIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fedipick = models.CharField(db_column='FEDIPICK', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fconfwhen = models.CharField(db_column='FCONFWHEN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fconfwho = models.CharField(db_column='FCONFWHO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpickwho = models.CharField(db_column='FPICKWHO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpickdte = models.CharField(db_column='FPICKDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchepcust = models.CharField(db_column='FCHEPCUST', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcedi = models.CharField(db_column='FCEDI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcedisdte = models.CharField(db_column='FCEDISDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcedistme = models.CharField(db_column='FCEDISTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fgroupcode = models.CharField(db_column='FGROUPCODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fsig = models.CharField(db_column='FSIG', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcpc = models.CharField(db_column='FCPC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchedi = models.CharField(db_column='FCHEDI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchedisdte = models.CharField(db_column='FCHEDISDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchedistme = models.CharField(db_column='FCHEDISTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    finbatch = models.CharField(db_column='FINBATCH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    flabeltype = models.CharField(db_column='FLABELTYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    forgsched = models.CharField(db_column='FORGSCHED', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcrtebymod = models.CharField(db_column='FCRTEBYMOD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpalreq = models.CharField(db_column='FPALREQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchepreq = models.CharField(db_column='FCHEPREQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcpcreq = models.CharField(db_column='FCPCREQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fothreq = models.CharField(db_column='FOTHREQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ftempovr = models.CharField(db_column='FTEMPOVR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    figpsreq = models.CharField(db_column='FIGPSREQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    figps = models.CharField(db_column='FIGPS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcustdata = models.CharField(db_column='FCUSTDATA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ftmphppzne = models.CharField(db_column='FTMPHPPZNE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    custkey = models.CharField(max_length=40, blank=True, null=True)
    datedt = models.DateTimeField(db_column='dateDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shipment_master'


class ShipmentMasterIntermediate(models.Model):
    newdata = models.IntegerField(db_column='newData', blank=True, null=True)  # Field name made lowercase.
    facilityid = models.CharField(db_column='facilityId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fbatch = models.CharField(db_column='FBATCH', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fcustcode = models.CharField(db_column='FCUSTCODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    floadnum = models.CharField(db_column='FLOADNUM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ftrailer = models.CharField(db_column='FTRAILER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fdoor = models.CharField(db_column='FDOOR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fpurchord = models.CharField(db_column='FPURCHORD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fsalesord = models.CharField(db_column='FSALESORD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fshipment = models.CharField(db_column='FSHIPMENT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fcustbol = models.CharField(db_column='FCUSTBOL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fdropnum = models.IntegerField(db_column='FDROPNUM', blank=True, null=True)  # Field name made lowercase.
    fbdate = models.CharField(db_column='FBDATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    forgdeldte = models.CharField(db_column='FORGDELDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    factdeldte = models.CharField(db_column='FACTDELDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fshipstat = models.CharField(db_column='FSHIPSTAT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    finuse = models.CharField(db_column='FINUSE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fltime = models.CharField(db_column='FLTIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcrosscust = models.CharField(db_column='FCROSSCUST', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fconscode = models.CharField(db_column='FCONSCODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fconsignee = models.CharField(db_column='FCONSIGNEE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    faddress1 = models.CharField(db_column='FADDRESS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    faddress2 = models.CharField(db_column='FADDRESS2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcity = models.CharField(db_column='FCITY', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fstate = models.CharField(db_column='FSTATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    destzip = models.CharField(db_column='DestZip', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fphone = models.CharField(db_column='FPHONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fseal = models.CharField(db_column='FSEAL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    carrierid = models.CharField(db_column='CarrierID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcheckqty = models.FloatField(db_column='FCHECKQTY', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    totalcube = models.FloatField(db_column='TotalCube', blank=True, null=True)  # Field name made lowercase.
    fcomment = models.CharField(db_column='FCOMMENT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fnotes = models.CharField(db_column='FNOTES', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ftemp = models.CharField(db_column='FTEMP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ffronttemp = models.CharField(db_column='FFRONTTEMP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fmidtemp = models.CharField(db_column='FMIDTEMP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fbacktemp = models.CharField(db_column='FBACKTEMP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fpaymethod = models.CharField(db_column='FPAYMETHOD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ftranmeth = models.CharField(db_column='FTRANMETH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fmbol = models.CharField(db_column='FMBOL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpickprint = models.CharField(db_column='FPICKPRINT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ftrancust = models.CharField(db_column='FTRANCUST', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fbilldoc = models.CharField(db_column='FBILLDOC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffulpalbil = models.CharField(db_column='FFULPALBIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcsepckbil = models.CharField(db_column='FCSEPCKBIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    flnechrbil = models.CharField(db_column='FLNECHRBIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fexportcty = models.CharField(db_column='FEXPORTCTY', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscansttme = models.CharField(db_column='FSCANSTTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscanstdte = models.CharField(db_column='FSCANSTDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscanentme = models.CharField(db_column='FSCANENTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscanendte = models.CharField(db_column='FSCANENDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscanbatch = models.CharField(db_column='FSCANBATCH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscanstat = models.CharField(db_column='FSCANSTAT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    feditype = models.CharField(db_column='FEDITYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fedi = models.CharField(db_column='FEDI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fedisnddte = models.CharField(db_column='FEDISNDDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fedisndtme = models.CharField(db_column='FEDISNDTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    foedi = models.CharField(db_column='FOEDI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    foedisdte = models.CharField(db_column='FOEDISDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    foedistme = models.CharField(db_column='FOEDISTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpalexchng = models.CharField(db_column='FPALEXCHNG', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpalcond = models.CharField(db_column='FPALCOND', max_length=30, blank=True, null=True)  # Field name made lowercase.
    floadoptcd = models.CharField(db_column='FLOADOPTCD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdtecngrsn = models.CharField(db_column='FDTECNGRSN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcarcngrsn = models.CharField(db_column='FCARCNGRSN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fversion = models.CharField(db_column='FVERSION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpallets = models.CharField(db_column='FPALLETS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchep = models.CharField(db_column='FCHEP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    farrivedte = models.CharField(db_column='FARRIVEDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    farrivetme = models.CharField(db_column='FARRIVETME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fstartdte = models.CharField(db_column='FSTARTDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fstarttme = models.CharField(db_column='FSTARTTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffinishdte = models.CharField(db_column='FFINISHDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffinishtme = models.CharField(db_column='FFINISHTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolorder = models.CharField(db_column='FCOLORDER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolwhse = models.CharField(db_column='FCOLWHSE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolneq = models.CharField(db_column='FCOLNEQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolqa = models.CharField(db_column='FCOLQA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolother = models.CharField(db_column='FCOLOTHER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolcoment = models.CharField(db_column='FCOLCOMENT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzorder = models.CharField(db_column='FFRZORDER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzwhse = models.CharField(db_column='FFRZWHSE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzneq = models.CharField(db_column='FFRZNEQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzqa = models.CharField(db_column='FFRZQA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzother = models.CharField(db_column='FFRZOTHER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzcoment = models.CharField(db_column='FFRZCOMENT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdryorder = models.CharField(db_column='FDRYORDER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdrywhse = models.CharField(db_column='FDRYWHSE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdryneq = models.CharField(db_column='FDRYNEQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdryqa = models.CharField(db_column='FDRYQA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdryother = models.CharField(db_column='FDRYOTHER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdrycoment = models.CharField(db_column='FDRYCOMENT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fconfirmnm = models.CharField(db_column='FCONFIRMNM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    flivedrop = models.CharField(db_column='FLIVEDROP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fschcoment = models.CharField(db_column='FSCHCOMENT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fsignoutme = models.CharField(db_column='FSIGNOUTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fsignoudte = models.CharField(db_column='FSIGNOUDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdriver = models.CharField(db_column='FDRIVER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fplanned = models.CharField(db_column='FPLANNED', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fwho = models.CharField(db_column='FWHO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdatestamp = models.CharField(db_column='FDATESTAMP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ftimestamp = models.CharField(db_column='FTIMESTAMP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fwhoship = models.CharField(db_column='FWHOSHIP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fshipdate = models.CharField(db_column='FSHIPDATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fshiptime = models.CharField(db_column='FSHIPTIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fedipick = models.CharField(db_column='FEDIPICK', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fconfwhen = models.CharField(db_column='FCONFWHEN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fconfwho = models.CharField(db_column='FCONFWHO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpickwho = models.CharField(db_column='FPICKWHO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpickdte = models.CharField(db_column='FPICKDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchepcust = models.CharField(db_column='FCHEPCUST', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcedi = models.CharField(db_column='FCEDI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcedisdte = models.CharField(db_column='FCEDISDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcedistme = models.CharField(db_column='FCEDISTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fgroupcode = models.CharField(db_column='FGROUPCODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fsig = models.CharField(db_column='FSIG', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcpc = models.CharField(db_column='FCPC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchedi = models.CharField(db_column='FCHEDI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchedisdte = models.CharField(db_column='FCHEDISDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchedistme = models.CharField(db_column='FCHEDISTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    finbatch = models.CharField(db_column='FINBATCH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    flabeltype = models.CharField(db_column='FLABELTYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    forgsched = models.CharField(db_column='FORGSCHED', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcrtebymod = models.CharField(db_column='FCRTEBYMOD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpalreq = models.CharField(db_column='FPALREQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchepreq = models.CharField(db_column='FCHEPREQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcpcreq = models.CharField(db_column='FCPCREQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fothreq = models.CharField(db_column='FOTHREQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ftempovr = models.CharField(db_column='FTEMPOVR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    figpsreq = models.CharField(db_column='FIGPSREQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    figps = models.CharField(db_column='FIGPS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcustdata = models.CharField(db_column='FCUSTDATA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ftmphppzne = models.CharField(db_column='FTMPHPPZNE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    custkey = models.CharField(max_length=40, blank=True, null=True)
    datedt = models.DateTimeField(db_column='dateDT', blank=True, null=True)  # Field name made lowercase.
    originzip = models.CharField(db_column='OriginZip', max_length=20, blank=True, null=True)  # Field name made lowercase.
    custname = models.CharField(db_column='custName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shipment_master_intermediate'


class ShipmentMasterLatLon(models.Model):
    newdata = models.IntegerField(db_column='newData', blank=True, null=True)  # Field name made lowercase.
    facilityid = models.CharField(db_column='facilityId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fbatch = models.CharField(db_column='FBATCH', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fcustcode = models.CharField(db_column='FCUSTCODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    floadnum = models.CharField(db_column='FLOADNUM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ftrailer = models.CharField(db_column='FTRAILER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fdoor = models.CharField(db_column='FDOOR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fpurchord = models.CharField(db_column='FPURCHORD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fsalesord = models.CharField(db_column='FSALESORD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fshipment = models.CharField(db_column='FSHIPMENT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fcustbol = models.CharField(db_column='FCUSTBOL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fdropnum = models.IntegerField(db_column='FDROPNUM', blank=True, null=True)  # Field name made lowercase.
    fbdate = models.CharField(db_column='FBDATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    forgdeldte = models.CharField(db_column='FORGDELDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    factdeldte = models.CharField(db_column='FACTDELDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fshipstat = models.CharField(db_column='FSHIPSTAT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    finuse = models.CharField(db_column='FINUSE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fltime = models.CharField(db_column='FLTIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcrosscust = models.CharField(db_column='FCROSSCUST', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fconscode = models.CharField(db_column='FCONSCODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fconsignee = models.CharField(db_column='FCONSIGNEE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    faddress1 = models.CharField(db_column='FADDRESS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    faddress2 = models.CharField(db_column='FADDRESS2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcity = models.CharField(db_column='FCITY', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fstate = models.CharField(db_column='FSTATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    destzip = models.CharField(db_column='DestZip', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fphone = models.CharField(db_column='FPHONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fseal = models.CharField(db_column='FSEAL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    carrierid = models.CharField(db_column='CarrierID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcheckqty = models.FloatField(db_column='FCHECKQTY', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    totalcube = models.FloatField(db_column='TotalCube', blank=True, null=True)  # Field name made lowercase.
    fcomment = models.CharField(db_column='FCOMMENT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fnotes = models.CharField(db_column='FNOTES', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ftemp = models.CharField(db_column='FTEMP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ffronttemp = models.CharField(db_column='FFRONTTEMP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fmidtemp = models.CharField(db_column='FMIDTEMP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fbacktemp = models.CharField(db_column='FBACKTEMP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fpaymethod = models.CharField(db_column='FPAYMETHOD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ftranmeth = models.CharField(db_column='FTRANMETH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fmbol = models.CharField(db_column='FMBOL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpickprint = models.CharField(db_column='FPICKPRINT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ftrancust = models.CharField(db_column='FTRANCUST', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fbilldoc = models.CharField(db_column='FBILLDOC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffulpalbil = models.CharField(db_column='FFULPALBIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcsepckbil = models.CharField(db_column='FCSEPCKBIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    flnechrbil = models.CharField(db_column='FLNECHRBIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fexportcty = models.CharField(db_column='FEXPORTCTY', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscansttme = models.CharField(db_column='FSCANSTTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscanstdte = models.CharField(db_column='FSCANSTDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscanentme = models.CharField(db_column='FSCANENTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscanendte = models.CharField(db_column='FSCANENDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscanbatch = models.CharField(db_column='FSCANBATCH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fscanstat = models.CharField(db_column='FSCANSTAT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    feditype = models.CharField(db_column='FEDITYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fedi = models.CharField(db_column='FEDI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fedisnddte = models.CharField(db_column='FEDISNDDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fedisndtme = models.CharField(db_column='FEDISNDTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    foedi = models.CharField(db_column='FOEDI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    foedisdte = models.CharField(db_column='FOEDISDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    foedistme = models.CharField(db_column='FOEDISTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpalexchng = models.CharField(db_column='FPALEXCHNG', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpalcond = models.CharField(db_column='FPALCOND', max_length=30, blank=True, null=True)  # Field name made lowercase.
    floadoptcd = models.CharField(db_column='FLOADOPTCD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdtecngrsn = models.CharField(db_column='FDTECNGRSN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcarcngrsn = models.CharField(db_column='FCARCNGRSN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fversion = models.CharField(db_column='FVERSION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpallets = models.CharField(db_column='FPALLETS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchep = models.CharField(db_column='FCHEP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    farrivedte = models.CharField(db_column='FARRIVEDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    farrivetme = models.CharField(db_column='FARRIVETME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fstartdte = models.CharField(db_column='FSTARTDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fstarttme = models.CharField(db_column='FSTARTTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffinishdte = models.CharField(db_column='FFINISHDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffinishtme = models.CharField(db_column='FFINISHTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolorder = models.CharField(db_column='FCOLORDER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolwhse = models.CharField(db_column='FCOLWHSE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolneq = models.CharField(db_column='FCOLNEQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolqa = models.CharField(db_column='FCOLQA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolother = models.CharField(db_column='FCOLOTHER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcolcoment = models.CharField(db_column='FCOLCOMENT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzorder = models.CharField(db_column='FFRZORDER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzwhse = models.CharField(db_column='FFRZWHSE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzneq = models.CharField(db_column='FFRZNEQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzqa = models.CharField(db_column='FFRZQA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzother = models.CharField(db_column='FFRZOTHER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ffrzcoment = models.CharField(db_column='FFRZCOMENT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdryorder = models.CharField(db_column='FDRYORDER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdrywhse = models.CharField(db_column='FDRYWHSE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdryneq = models.CharField(db_column='FDRYNEQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdryqa = models.CharField(db_column='FDRYQA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdryother = models.CharField(db_column='FDRYOTHER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdrycoment = models.CharField(db_column='FDRYCOMENT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fconfirmnm = models.CharField(db_column='FCONFIRMNM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    flivedrop = models.CharField(db_column='FLIVEDROP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fschcoment = models.CharField(db_column='FSCHCOMENT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fsignoutme = models.CharField(db_column='FSIGNOUTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fsignoudte = models.CharField(db_column='FSIGNOUDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdriver = models.CharField(db_column='FDRIVER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fplanned = models.CharField(db_column='FPLANNED', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fwho = models.CharField(db_column='FWHO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdatestamp = models.CharField(db_column='FDATESTAMP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ftimestamp = models.CharField(db_column='FTIMESTAMP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fwhoship = models.CharField(db_column='FWHOSHIP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fshipdate = models.CharField(db_column='FSHIPDATE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fshiptime = models.CharField(db_column='FSHIPTIME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fedipick = models.CharField(db_column='FEDIPICK', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fconfwhen = models.CharField(db_column='FCONFWHEN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fconfwho = models.CharField(db_column='FCONFWHO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpickwho = models.CharField(db_column='FPICKWHO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpickdte = models.CharField(db_column='FPICKDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchepcust = models.CharField(db_column='FCHEPCUST', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcedi = models.CharField(db_column='FCEDI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcedisdte = models.CharField(db_column='FCEDISDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcedistme = models.CharField(db_column='FCEDISTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fgroupcode = models.CharField(db_column='FGROUPCODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fsig = models.CharField(db_column='FSIG', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcpc = models.CharField(db_column='FCPC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchedi = models.CharField(db_column='FCHEDI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchedisdte = models.CharField(db_column='FCHEDISDTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchedistme = models.CharField(db_column='FCHEDISTME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    finbatch = models.CharField(db_column='FINBATCH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    flabeltype = models.CharField(db_column='FLABELTYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    forgsched = models.CharField(db_column='FORGSCHED', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcrtebymod = models.CharField(db_column='FCRTEBYMOD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fpalreq = models.CharField(db_column='FPALREQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fchepreq = models.CharField(db_column='FCHEPREQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcpcreq = models.CharField(db_column='FCPCREQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fothreq = models.CharField(db_column='FOTHREQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ftempovr = models.CharField(db_column='FTEMPOVR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    figpsreq = models.CharField(db_column='FIGPSREQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    figps = models.CharField(db_column='FIGPS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fcustdata = models.CharField(db_column='FCUSTDATA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ftmphppzne = models.CharField(db_column='FTMPHPPZNE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    custkey = models.CharField(max_length=40, blank=True, null=True)
    datedt = models.DateTimeField(db_column='dateDT', blank=True, null=True)  # Field name made lowercase.
    originzip = models.CharField(db_column='OriginZip', max_length=20, blank=True, null=True)  # Field name made lowercase.
    custname = models.CharField(db_column='custName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    origin_lat = models.FloatField(blank=True, null=True)
    origin_lon = models.FloatField(blank=True, null=True)
    origin_std_city = models.CharField(max_length=100, blank=True, null=True)
    origin_std_state = models.CharField(max_length=20, blank=True, null=True)
    origin_coord_name = models.CharField(max_length=100, blank=True, null=True)
    dest_lat = models.FloatField(blank=True, null=True)
    dest_lon = models.FloatField(blank=True, null=True)
    dest_std_city = models.CharField(max_length=100, blank=True, null=True)
    dest_std_state = models.CharField(max_length=20, blank=True, null=True)
    dest_coord_name = models.CharField(max_length=100, blank=True, null=True)
    overlap = models.IntegerField()
    carriername = models.CharField(db_column='carrierName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shipment_master_lat_lon'


class Warehouses(models.Model):
    prefix = models.CharField(max_length=10, blank=True, null=True)
    native = models.CharField(max_length=20, blank=True, null=True)
    whid = models.CharField(max_length=20, blank=True, null=True)
    whname = models.CharField(max_length=100, blank=True, null=True)
    addr1 = models.CharField(max_length=100, blank=True, null=True)
    addr2 = models.CharField(max_length=100, blank=True, null=True)
    addr3 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    whid_join = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'warehouses'


class Zips(models.Model):
    zip = models.CharField(primary_key=True, max_length=10)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    timezone = models.FloatField(blank=True, null=True)
    dst = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zips'


class Zips2(models.Model):
    zip = models.CharField(primary_key=True, max_length=10)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    timezone = models.FloatField(blank=True, null=True)
    dst = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zips2'
