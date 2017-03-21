class stage01_resequencing_omniExpressExome_dependencies():
    def make_mutationID(self,Chr,MapInfo):
        """Return unique mutation id based on the
        chromosome and position

        Args
            Chr (str)
            MapInfo (int)
    
        Returns
            id_O (str)
        """

        id_O = '%s_%s'%(Chr,MapInfo)
        return id_O;