import properties
import prepareVectors
import tournament

properties.call_properties_layout("/home/federico/Tesi/Dataset")
prepareVectors.prepare_layout_vector("/home/federico/Tesi/Dataset")
tournament.do_tournament()