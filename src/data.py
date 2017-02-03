import numpy as np
import holoviews as hv
import IPython.display

class Data:
    def __init__(self):
        self.index = np.linspace(0, 10, 101)

    def signal(self, index):     
        t = np.linspace(0, 3.14, 101)
        return np.sin(2*np.pi*index*t)
    
    def signal2D(self, index):
        t = np.linspace(-10, 10, 11)
        X, Y = np.meshgrid(t, t)
        return np.sin(2*np.pi*index*(X**2 + Y**2))


class DataAnalysis:
    def __init__(self, data):
        self.data = data
        self.slider = ipywidgets.IntSlider(value=self.data.index[0],
                                           min=self.data.index[0], 
                                           max=self.data.index[-1])
    def _ipython_display_(self):
        IPython.display.display(self.slider)


class DataAnalysisHoloviews:
    def __init__(self, data, dynamic=False):
        self.data = data
        
        # The self._ipython_display function is set here, depending
        # on whether we choose the analysis to be dynamic or not.
        
        self._ipython_display_ = self._ipython_display_holomap_
        if dynamic:
            self._ipython_display_ = self._ipython_display_dynamicmap_

    def _signal(self, index):
        """
        This function wraps the signal function from the data class and transforms
        the data into a HoloViws object.
        """

        return hv.Curve(self.data.signal(index))
    
    def _ipython_display_holomap_(self):
        """
        This function creates a static HoloMap from the data, and
        returns an object which the Notebook can display
        """
        self._map_object = hv.HoloMap([(i, self._signal(i)) for i in self.data.index],
                      kdims=[hv.Dimension(name='Index',
                                          label='Index',
                                          values=list(self.data.index))])

        return IPython.display.display(self._map_object)

    def _ipython_display_dynamicmap_(self):
        """
        This function creates a dynamic HoloMap from the data,
        and returns an object which the Notebook can display
        """
        self._map_object = hv.DynamicMap(self._signal,
                      kdims=[hv.Dimension(name='Index',
                                          label='Index',
                                          values=list(self.data.index))])

        return IPython.display.display(self._map_object)
