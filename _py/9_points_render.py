################################################################################
###                                                                          ###
###   GH_Gcode for TL                                                        ###
###                                                                          ###
###       Component : Points Render / 201123                                 ###
###                                                                          ###
###                                                                          ###
###   Base Script >>> GH_Gcode                                               ###
###                                                                          ###
###       Repository : https://github.com/naysok/GH_Gcode                    ###
###       Coding : naoki yoshioka (naysok)                                   ###
###       License : MIT License                                              ###
###                                                                          ###
################################################################################


import datetime
import math


class Util():


    def get_current_time(self):
        return str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))


    def remap_number(self, src, old_min, old_max, new_min, new_max):
        return ((src - old_min) / (old_max - old_min) * (new_max - new_min) + new_min)


    def flatten_runtime_list(self, list):
        all = []
        
        for i in xrange(len(list)):
            # print(i)
            sub = list[i]
            for j in xrange(len(sub)):
                # print(j)
                all.append(sub[j])

        return all


    def export_gcode(self, dir_path, txt):

        now = self.get_current_time()
        file_path = dir_path + now + ".gcode"

        ### Export
        with open(file_path, 'w') as f:
            f.write(txt)

        print("Export GCode : {}".format(file_path))


    def zip_matrix(self, mat):
        ### https://note.nkmk.me/python-list-transpose/
        return [list(x) for x in zip(*mat)]


    def padding_previous_value(self, list_):
        
        list_pad = []

        for i in xrange(len(list_)):
            
            item_ = list_[i]

            ### First 
            if i == 0:
                if (item_ == None):
                    list_pad.append(0)
                else:
                    list_pad.append(item_)
            
            ### Not Frist
            else:
                if (item_ == None):
                    tmp = list_pad[i-1]
                    list_pad.append(tmp)
                else:
                    list_pad.append(item_)
        
        return list_pad


    def remove_previous_elements(self, a_list):

        ### Remove Same Element as the Previous One
        new_list = []
        src_length = len(a_list)

        for i in range(src_length):
            tmp = a_list[i]

            ### 
            if i < src_length-1:
                if a_list[i] != a_list[i+1]:
                    new_list.append(tmp)
            ### Last
            else:
                new_list.append(tmp)
                
        return new_list


    def bitwise_or_arrays(self, arrays):

        ### Merge Bool from Brep.isPointInside

        # print(len(arrays[0]))
        # print(len(arrays[0][0]))

        if len(arrays) == 1:
            return arrays[0]

        else:
            arrays_zip = self.zip_matrix(arrays)
            # print(len(arrays_zip))
            # print(len(arrays_zip[0]))
            # print(len(arrays_zip[0][0]))

            bool_inside = []

            for i in xrange(len(arrays_zip)):
                # print(i)

                sub_ = []

                item = arrays_zip[i]
                item_zip = self.zip_matrix(item)

                # print(len(item_zip))
                # print(len(item_zip[0]))

                for j in xrange(len(item_zip)):

                    values = item_zip[j]
                    
                    if True in values:
                        sub_.append(True)
                    else:
                        sub_.append(False)

                bool_inside.append(sub_)

            # print(len(bool_inside))
            # print(len(bool_inside[0]))

            return bool_inside

ut = Util()


##########

##########


ghenv.Component.Message = 'Points Render / 201123'


if __DRAW:
    __DRAW_POINTS = ut.flatten_runtime_list(POINTS)