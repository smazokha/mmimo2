#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: mMIMO Capture
# GNU Radio version: v3.8.5.0-6-g57bd109d

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time

from gnuradio import qtgui

class wifi_4usrp_native(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "mMIMO Capture")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("mMIMO Capture")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "wifi_4usrp_native")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.skip_num_items = skip_num_items = 1000000
        self.samp_rate = samp_rate = 5e6
        self.record_num_items = record_num_items = 2000000
        self.gain = gain = 0
        self.freq = freq = 2485e6

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0_2 = uhd.usrp_source(
            ",".join(("addr=10.10.24.5", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,2)),
            ),
        )
        self.uhd_usrp_source_0_2.set_time_unknown_pps(uhd.time_spec())
        now = self.uhd_usrp_source_0_2.get_time_now()
        start_time = now + uhd.time_spec(.5)
        self.uhd_usrp_source_0_2.set_command_time(start_time)
        self.uhd_usrp_source_0_2.set_subdev_spec('A:0 B:0', 0)
        self.uhd_usrp_source_0_2.set_time_source('external', 0)
        self.uhd_usrp_source_0_2.set_clock_source('external', 0)
        self.uhd_usrp_source_0_2.set_center_freq(freq, 0)
        self.uhd_usrp_source_0_2.set_gain(gain, 0)
        self.uhd_usrp_source_0_2.set_antenna('RX2', 0)
        self.uhd_usrp_source_0_2.set_center_freq(freq, 1)
        self.uhd_usrp_source_0_2.set_gain(gain, 1)
        self.uhd_usrp_source_0_2.set_antenna('RX2', 1)
        self.uhd_usrp_source_0_2.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_2.clear_command_time()

        self.uhd_usrp_source_0_1_1 = uhd.usrp_source(
            ",".join(("addr=10.10.24.7", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,2)),
            ),
        )
        self.uhd_usrp_source_0_1_1.set_time_unknown_pps(uhd.time_spec())
        now = self.uhd_usrp_source_0_1_1.get_time_now()
        start_time = now + uhd.time_spec(.5)
        self.uhd_usrp_source_0_1_1.set_command_time(start_time)
        self.uhd_usrp_source_0_1_1.set_subdev_spec('A:0 B:0', 0)
        self.uhd_usrp_source_0_1_1.set_time_source('external', 0)
        self.uhd_usrp_source_0_1_1.set_clock_source('external', 0)
        self.uhd_usrp_source_0_1_1.set_center_freq(freq, 0)
        self.uhd_usrp_source_0_1_1.set_gain(gain, 0)
        self.uhd_usrp_source_0_1_1.set_antenna('RX2', 0)
        self.uhd_usrp_source_0_1_1.set_center_freq(freq, 1)
        self.uhd_usrp_source_0_1_1.set_gain(gain, 1)
        self.uhd_usrp_source_0_1_1.set_antenna('RX2', 1)
        self.uhd_usrp_source_0_1_1.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_1_1.clear_command_time()

        self.uhd_usrp_source_0_1_0_0 = uhd.usrp_source(
            ",".join(("addr=10.10.24.8", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,2)),
            ),
        )

        self.uhd_usrp_source_0_1_0_0.set_time_unknown_pps(uhd.time_spec())
        now = self.uhd_usrp_source_0_1_0_0.get_time_now()
        start_time = now + uhd.time_spec(.5)
        self.uhd_usrp_source_0_1_0_0.set_command_time(start_time)
        self.uhd_usrp_source_0_1_0_0.set_subdev_spec('A:0 B:0', 0)
        self.uhd_usrp_source_0_1_0_0.set_time_source('external', 0)
        self.uhd_usrp_source_0_1_0_0.set_clock_source('external', 0)
        self.uhd_usrp_source_0_1_0_0.set_center_freq(freq, 0)
        self.uhd_usrp_source_0_1_0_0.set_gain(gain, 0)
        self.uhd_usrp_source_0_1_0_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0_1_0_0.set_center_freq(freq, 1)
        self.uhd_usrp_source_0_1_0_0.set_gain(gain, 1)
        self.uhd_usrp_source_0_1_0_0.set_antenna('RX2', 1)
        self.uhd_usrp_source_0_1_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_1_0_0.clear_command_time()

        self.uhd_usrp_source_0_0_0 = uhd.usrp_source(
            ",".join(("addr=10.10.24.6", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,2)),
            ),
        )

        self.uhd_usrp_source_0_0_0.set_time_unknown_pps(uhd.time_spec())
        now = self.uhd_usrp_source_0_0_0.get_time_now()
        start_time = now + uhd.time_spec(.5)
        self.uhd_usrp_source_0_0_0.set_command_time(start_time)
        self.uhd_usrp_source_0_0_0.set_time_source('external', 0)
        self.uhd_usrp_source_0_0_0.set_clock_source('external', 0)
        self.uhd_usrp_source_0_0_0.set_center_freq(freq, 0)
        self.uhd_usrp_source_0_0_0.set_gain(gain, 0)
        self.uhd_usrp_source_0_0_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0_0_0.set_center_freq(freq, 1)
        self.uhd_usrp_source_0_0_0.set_gain(gain, 1)
        self.uhd_usrp_source_0_0_0.set_antenna('RX2', 1)
        self.uhd_usrp_source_0_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0_0.clear_command_time()

        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join(("addr=10.10.24.4", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            '',
        )
        self.uhd_usrp_sink_0.set_subdev_spec('A:0', 0)
        self.uhd_usrp_sink_0.set_time_source('external', 0)
        self.uhd_usrp_sink_0.set_clock_source('external', 0)
        self.uhd_usrp_sink_0.set_center_freq(freq, 0)
        self.uhd_usrp_sink_0.set_gain(gain, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_time_unknown_pps(uhd.time_spec())
        self.qtgui_freq_sink_x_3_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1
        )
        self.qtgui_freq_sink_x_3_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_3_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_3_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_3_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_3_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_3_0.enable_grid(False)
        self.qtgui_freq_sink_x_3_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_3_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_3_0.enable_control_panel(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_3_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_3_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_3_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_3_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_3_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_3_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_3_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_3_0_win)
        self.qtgui_freq_sink_x_3 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1
        )
        self.qtgui_freq_sink_x_3.set_update_time(0.10)
        self.qtgui_freq_sink_x_3.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_3.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_3.enable_autoscale(False)
        self.qtgui_freq_sink_x_3.enable_grid(False)
        self.qtgui_freq_sink_x_3.set_fft_average(1.0)
        self.qtgui_freq_sink_x_3.enable_axis_labels(True)
        self.qtgui_freq_sink_x_3.enable_control_panel(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_3.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_3.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_3.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_3.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_3.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_3_win = sip.wrapinstance(self.qtgui_freq_sink_x_3.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_3_win)
        self.blocks_skiphead_7_0 = blocks.skiphead(gr.sizeof_gr_complex*1, skip_num_items)
        self.blocks_skiphead_6_0 = blocks.skiphead(gr.sizeof_gr_complex*1, skip_num_items)
        self.blocks_skiphead_4_0_0 = blocks.skiphead(gr.sizeof_gr_complex*1, skip_num_items)
        self.blocks_skiphead_4_0 = blocks.skiphead(gr.sizeof_gr_complex*1, skip_num_items)
        self.blocks_skiphead_3_0 = blocks.skiphead(gr.sizeof_gr_complex*1, skip_num_items)
        self.blocks_skiphead_2_0 = blocks.skiphead(gr.sizeof_gr_complex*1, skip_num_items)
        self.blocks_skiphead_1_0 = blocks.skiphead(gr.sizeof_gr_complex*1, skip_num_items)
        self.blocks_skiphead_0_0 = blocks.skiphead(gr.sizeof_gr_complex*1, skip_num_items)
        self.blocks_head_8_0 = blocks.head(gr.sizeof_gr_complex*1, record_num_items)
        self.blocks_head_7_0 = blocks.head(gr.sizeof_gr_complex*1, record_num_items)
        self.blocks_head_6_0 = blocks.head(gr.sizeof_gr_complex*1, record_num_items)
        self.blocks_head_5_0 = blocks.head(gr.sizeof_gr_complex*1, record_num_items)
        self.blocks_head_4_0 = blocks.head(gr.sizeof_gr_complex*1, record_num_items)
        self.blocks_head_3_0 = blocks.head(gr.sizeof_gr_complex*1, record_num_items)
        self.blocks_head_1_0_0 = blocks.head(gr.sizeof_gr_complex*1, record_num_items)
        self.blocks_head_1_0 = blocks.head(gr.sizeof_gr_complex*1, record_num_items)
        self.blocks_file_sink_7_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/root/24-8_chA.bin', False)
        self.blocks_file_sink_7_0.set_unbuffered(False)
        self.blocks_file_sink_6_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/root/24-7_chB.bin', False)
        self.blocks_file_sink_6_0.set_unbuffered(False)
        self.blocks_file_sink_5_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/root/24-7_chA.bin', False)
        self.blocks_file_sink_5_0.set_unbuffered(False)
        self.blocks_file_sink_4_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/root/24-8_chB.bin', False)
        self.blocks_file_sink_4_0.set_unbuffered(False)
        self.blocks_file_sink_3_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/root/24-6_chB.bin', False)
        self.blocks_file_sink_3_0.set_unbuffered(False)
        self.blocks_file_sink_2_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/root/24-6_chA.bin', False)
        self.blocks_file_sink_2_0.set_unbuffered(False)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/root/24-5_chB.bin', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/root/24-5_chA.bin', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 2e6, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_head_1_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_head_1_0_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.blocks_head_3_0, 0), (self.blocks_file_sink_2_0, 0))
        self.connect((self.blocks_head_4_0, 0), (self.blocks_file_sink_3_0, 0))
        self.connect((self.blocks_head_5_0, 0), (self.blocks_file_sink_7_0, 0))
        self.connect((self.blocks_head_6_0, 0), (self.blocks_file_sink_5_0, 0))
        self.connect((self.blocks_head_7_0, 0), (self.blocks_file_sink_6_0, 0))
        self.connect((self.blocks_head_8_0, 0), (self.blocks_file_sink_4_0, 0))
        self.connect((self.blocks_skiphead_0_0, 0), (self.blocks_head_3_0, 0))
        self.connect((self.blocks_skiphead_1_0, 0), (self.blocks_head_4_0, 0))
        self.connect((self.blocks_skiphead_2_0, 0), (self.blocks_head_5_0, 0))
        self.connect((self.blocks_skiphead_3_0, 0), (self.blocks_head_8_0, 0))
        self.connect((self.blocks_skiphead_4_0, 0), (self.blocks_head_1_0, 0))
        self.connect((self.blocks_skiphead_4_0_0, 0), (self.blocks_head_1_0_0, 0))
        self.connect((self.blocks_skiphead_6_0, 0), (self.blocks_head_6_0, 0))
        self.connect((self.blocks_skiphead_7_0, 0), (self.blocks_head_7_0, 0))
        self.connect((self.uhd_usrp_source_0_0_0, 0), (self.blocks_skiphead_0_0, 0))
        self.connect((self.uhd_usrp_source_0_0_0, 1), (self.blocks_skiphead_1_0, 0))
        self.connect((self.uhd_usrp_source_0_1_0_0, 0), (self.blocks_skiphead_2_0, 0))
        self.connect((self.uhd_usrp_source_0_1_0_0, 1), (self.blocks_skiphead_3_0, 0))
        self.connect((self.uhd_usrp_source_0_1_1, 0), (self.blocks_skiphead_6_0, 0))
        self.connect((self.uhd_usrp_source_0_1_1, 1), (self.blocks_skiphead_7_0, 0))
        self.connect((self.uhd_usrp_source_0_2, 0), (self.blocks_skiphead_4_0, 0))
        self.connect((self.uhd_usrp_source_0_2, 1), (self.blocks_skiphead_4_0_0, 0))
        self.connect((self.uhd_usrp_source_0_2, 0), (self.qtgui_freq_sink_x_3, 0))
        self.connect((self.uhd_usrp_source_0_2, 1), (self.qtgui_freq_sink_x_3_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "wifi_4usrp_native")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_skip_num_items(self):
        return self.skip_num_items

    def set_skip_num_items(self, skip_num_items):
        self.skip_num_items = skip_num_items

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.qtgui_freq_sink_x_3.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_3_0.set_frequency_range(0, self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0_1_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0_1_1.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0_2.set_samp_rate(self.samp_rate)

    def get_record_num_items(self):
        return self.record_num_items

    def set_record_num_items(self, record_num_items):
        self.record_num_items = record_num_items
        self.blocks_head_1_0.set_length(self.record_num_items)
        self.blocks_head_1_0_0.set_length(self.record_num_items)
        self.blocks_head_3_0.set_length(self.record_num_items)
        self.blocks_head_4_0.set_length(self.record_num_items)
        self.blocks_head_5_0.set_length(self.record_num_items)
        self.blocks_head_6_0.set_length(self.record_num_items)
        self.blocks_head_7_0.set_length(self.record_num_items)
        self.blocks_head_8_0.set_length(self.record_num_items)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_sink_0.set_gain(self.gain, 0)
        self.uhd_usrp_source_0_0_0.set_gain(self.gain, 0)
        self.uhd_usrp_source_0_0_0.set_gain(self.gain, 1)
        self.uhd_usrp_source_0_1_0_0.set_gain(self.gain, 0)
        self.uhd_usrp_source_0_1_0_0.set_gain(self.gain, 1)
        self.uhd_usrp_source_0_1_1.set_gain(self.gain, 0)
        self.uhd_usrp_source_0_1_1.set_gain(self.gain, 1)
        self.uhd_usrp_source_0_2.set_gain(self.gain, 0)
        self.uhd_usrp_source_0_2.set_gain(self.gain, 1)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_sink_0.set_center_freq(self.freq, 0)
        self.uhd_usrp_source_0_0_0.set_center_freq(self.freq, 0)
        self.uhd_usrp_source_0_0_0.set_center_freq(self.freq, 1)
        self.uhd_usrp_source_0_1_0_0.set_center_freq(self.freq, 0)
        self.uhd_usrp_source_0_1_0_0.set_center_freq(self.freq, 1)
        self.uhd_usrp_source_0_1_1.set_center_freq(self.freq, 0)
        self.uhd_usrp_source_0_1_1.set_center_freq(self.freq, 1)
        self.uhd_usrp_source_0_2.set_center_freq(self.freq, 0)
        self.uhd_usrp_source_0_2.set_center_freq(self.freq, 1)





def main(top_block_cls=wifi_4usrp_native, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
