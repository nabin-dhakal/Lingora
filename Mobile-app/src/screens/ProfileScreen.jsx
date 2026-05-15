import {
    StyleSheet,
    View,
    Text,
    TextInput,
    TouchableOpacity,
    FlatList,
    Dimensions,
  } from "react-native";
import {useState} from "react";

const ProfileScreen = () => {
    const [profileData, setProfileData] = useState({
        name: "",
        email: "",
    });
    
    const handleInputChange = (field, value) => {
        setProfileData((prevData) => ({
            ...prevData,
            [field]: value,
        }));
    };

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Profile</Text>
            <View style={styles.inputContainer}>
                <Text>Name:</Text>
                <TextInput
                    style={styles.input}
                    value={profileData.name}
                    onChangeText={(text) => handleInputChange("name", text)}
                />
            </View>
            <View style={styles.inputContainer}>
                <Text>Email:</Text>
                <TextInput
                    style={styles.input}
                    value={profileData.email}
                    onChangeText={(text) => handleInputChange("email", text)}
                />
            </View>
            <TouchableOpacity style={styles.saveButton}>
                <Text style={styles.saveButtonText}>Save</Text>
            </TouchableOpacity>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 20,
    },
    title: {
        fontSize: 24,
        fontWeight: "bold",
        marginBottom: 20,
    },
    inputContainer: {
        marginBottom: 15,
    },
    input: {
        borderWidth: 1,
        borderColor: "#ccc",
        borderRadius: 5,
        padding: 10,
        marginTop: 5,
    },
    saveButton: {
        backgroundColor: "#1CB0F6",
        padding: 15,
        borderRadius: 5,
        alignItems: "center",
    },
    saveButtonText: {
        color: "#fff",
        fontWeight: "bold",
    },
});

export default ProfileScreen;
