import React from 'react';
import { StyleSheet, Text, View, Image } from 'react-native';
import styles from './Styles';
import { ScrollView, useWindowDimensions } from "react-native";
import HTML from "react-native-render-html";

const htmlContent = `
<div class="loading_screen border_class_1">
<div class="frame_1">
    <img class="wastenot_1" src="https://anima-uploads.s3.amazonaws.com/projects/5fa6a1504924a2c17b91be91/releases/5fa6d1aca7a1f7aa9f02dcb0/img/wastenot-1@2x.png" />
    <h1 class="wastenot valign-text-middle font_class_1 border_class_1">
        <span>
            <span class="span1_ZWxCAD">waste</span>
            <span class="span2_ZWxCAD">not.</span>
        </span>
    </h1>
</div>
</div>
`;

export default function SplashScreen() {
    return (
        <View style={[styles.loading_screen, styles.border_class_1]}>
            <View style={styles.frame_1}>
                <Image style={styles.wastenot_1} source={{ uri: 'https://anima-uploads.s3.amazonaws.com/projects/5fa6a1504924a2c17b91be91/releases/5fa6d1aca7a1f7aa9f02dcb0/img/wastenot-1@2x.png' }} />
                <View style={[styles.wastenot, styles.font_class_1]}>
                    <Text style={styles.span1_ZWxCAD}>waste<Text style={styles.span2_ZWxCAD}> not.</Text></Text>

                </View>
            </View>
        </View>
    );
}
