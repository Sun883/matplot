import pickle
import numpy.testing
from pandas import testing
import numpy as np
from pandas.api.types import is_numeric_dtype, is_datetime64_dtype

class TestPlots():

    @classmethod
    def setup_class(self):
       with open('test_file/actual.pickle', 'rb') as file:
            self.actual = pickle.load(file)
       with open('question/plot1.pickle', 'rb') as file:
            self.ax = pickle.load(file)
       with open('question/plot2.pickle', 'rb') as file:
            self.ax1 = pickle.load(file)
    
    @classmethod
    def extract_axis(self, axes):
        return [ax.get_text() for ax in axes]
    
    def test_ax_title(self):
        assert self.ax.axes.get_title() == self.actual["plot1"]["plot1_title"]

    def test_ax_y(self):
        assert self.extract_axis(list(self.ax.axes.yaxis.get_ticklabels())) == self.actual["plot1"]["plot1_y"]

    def test_ax_x(self):
        assert self.extract_axis(list(self.ax.axes.xaxis.get_ticklabels())) == self.actual["plot1"]["plot1_x"]

    def test_ax_width(self):
        assert self.ax.figure.get_figheight() == self.actual["plot1"]["plot1_height"]
    
    def test_ax_height(self):
        assert self.ax.figure.get_figwidth() == self.actual["plot1"]["plot1_width"]
        
    def test_ax_xlabel(self):
        assert self.ax.axes.get_xlabel() == self.actual["plot1"]["plot1_xtitle"]
        
    def test_ax_ylabel(self):
        assert self.ax.axes.get_ylabel() == self.actual["plot1"]["plot1_ytitle"]

    
    
    def test_ax1_title(self):
        assert self.ax1.axes.get_title() == self.actual["plot2"]["plot2_title"]

    def test_ax1_y(self):
        assert self.extract_axis(list(self.ax1.axes.yaxis.get_ticklabels())) == self.actual["plot2"]["plot2_y"]

    def test_ax1_x(self):
        assert self.extract_axis(list(self.ax1.axes.xaxis.get_ticklabels())) == self.actual["plot2"]["plot2_x"]

    def test_ax1_width(self):
        assert self.ax1.figure.get_figheight() == self.actual["plot2"]["plot2_height"]
    
    def test_ax1_height(self):
        assert self.ax1.figure.get_figwidth() == self.actual["plot2"]["plot2_width"]
        
    def test_ax1_xlabel(self):
        assert self.ax1.axes.get_xlabel() == self.actual["plot2"]["plot2_xtitle"]
        
    def test_ax1_ylabel(self):
        assert self.ax1.axes.get_ylabel() == self.actual["plot2"]["plot2_ytitle"]

